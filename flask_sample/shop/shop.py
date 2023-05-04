from flask import Blueprint, request, flash, render_template, redirect, url_for
from werkzeug.datastructures import MultiDict
from shop.forms import ProductForm, CheckoutForm
from sql.db import DB
from roles.permissions import admin_permission
from flask_login import login_required, current_user
shop = Blueprint('shop', __name__, url_prefix='/',template_folder='templates')


@shop.route("/admin/product", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def product():
    form = ProductForm()
    id = request.args.get("id", form.id.data or None)
    type = "Edit" if id else "Create"
    if form.validate_on_submit():
        if form.id.data:  # it's an update
            try:
                result = DB.update("UPDATE IS601_Products set name = %s, description = %s, stock = %s, cost = %s, image = %s, category = %s, visibility = %s WHERE id = %s",
                form.name.data, form.description.data, form.stock.data, form.cost.data, form.image.data, form.category.data, form.visibility.data, form.id.data)
                if result.status:
                    flash(f"Updated {form.name.data}", "success")
            except Exception as e:
                print("Error updating product", e)
                flash(f"Error updating product {form.name.data}", "danger")
        else:  # it's a create
            try:
                result = DB.update("""INSERT INTO IS601_Products (name, description, stock, cost, image, category, visibility) 
                VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                form.name.data, form.description.data, form.stock.data, form.cost.data, form.image.data, form.category.data, form.visibility.data)
                if result.status:
                    flash(f"Created {form.name.data}", "success")
                    form = ProductForm()  # clear form
            except Exception as e:
                print("Error creating product", e)
                flash(f"Error creating product {form.name.data}", "danger")
    if id:
        try:
            result = DB.selectOne("SELECT id, name, description, stock, cost, image, category, visibility FROM IS601_Products WHERE id = %s", id)
            if result.status and result.row:
                form.process(MultiDict(result.row))
        except Exception as e:
            print("Error fetching product", e)
            flash("Product not found", "danger")
    return render_template("product.html", form=form, type=type)


@shop.route("/admin/products/delete", methods=["GET"])
@admin_permission.require(http_exception=403)
def delete():
    id = request.args.get("id")
    if id:
        try:
            result = DB.delete("DELETE FROM IS601_Products WHERE id = %s", id)
            if result.status:
                flash("Deleted product", "success")
        except Exception as e:
            print("Error deleting product",e)
            flash("Error deleting product", "danger")
    return redirect(url_for("shop.products"))

@shop.route("/admin/products", methods=["GET","POST"])
@admin_permission.require(http_exception=403)
def products():
    rows = []
    try:
        result = DB.selectAll("SELECT id, name, description, stock, cost, image, visibility FROM IS601_Products LIMIT 25",)
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error fetching products", e)
        flash("There was a problem loading products", "danger")
    return render_template("products.html", rows=rows)

#gnb5 implemented on 4/21/23
@shop.route('/shop', methods=['GET'])
def shop_list():
    name = request.args.get("name")
    category = request.args.get("category")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)
    args = []

    query = "SELECT * FROM IS601_Products WHERE visibility = 1"

    if name:
        query += " AND name LIKE %s"
        args.append(f"%{name}%")
    
    if category:
        query += " AND category = %s"
        args.append(category)
    
    if order:
        if order in ["asc", "desc"]:
            query += f" ORDER BY cost {order}"
    
    if limit and int(limit) > 0 and int(limit) <= 100:
        query += " LIMIT %s"
        args.append(int(limit))
    
    rows = []
    try:
        resp = DB.selectAll(query, *args)
        if resp.status:
            rows = resp.rows
    except Exception as e:
        flash(str(e), "danger")

    # Get unique categories
    categories = []
    try:
        cat_resp = DB.selectAll("SELECT DISTINCT category FROM IS601_Products WHERE visibility = 1")
        if cat_resp.status:
            categories = [row['category'] for row in cat_resp.rows]
    except Exception as e:
        flash(str(e), "danger")

    return render_template("shop.html", products=rows, categories=categories)


#gnb5 4/18/23
@shop.route("/cart", methods=["GET","POST"])
@login_required
def cart():
    product_id = request.form.get("product_id")
    id = request.form.get("id", product_id)
    print("id", id)
    quantity = request.form.get("quantity", 1, type=int)
    user_id = current_user.get_id()
    if id and user_id:
        if quantity > 0:
            try:
                result = DB.selectOne("SELECT cost,name from IS601_Products WHERE id = %s", id)
                print("result", result)
                if result.status and result.row:
                    cost = result.row["cost"]
                    name = result.row["name"]
                    if product_id: # update from cart
                        result = DB.insertOne("""
                        UPDATE IS601_Cart SET
                        quantity = %(quantity)s,
                        cost = %(cost)s
                        WHERE product_id = %(id)s and user_id = %(user_id)s
                        """,{
                            "id":id,
                            "quantity": quantity,
                            "cost":cost,
                            "user_id":user_id
                        })
                        if result.status:
                            flash(f"Updated quantity for {name} to {quantity}", "success")
                    else: #add from shop
                        result = DB.insertOne("""
                        INSERT INTO IS601_Cart (product_id, quantity, cost, user_id)
                        VALUES(%(id)s, %(quantity)s, %(cost)s, %(user_id)s)
                        ON DUPLICATE KEY UPDATE
                        quantity = quantity + %(quantity)s,
                        cost = %(cost)s
                        """,{
                            "id":id,
                            "quantity": quantity,
                            "cost":cost,
                            "user_id":user_id
                        })
                        if result.status:
                            flash(f"Added {quantity} of {name} to cart", "success")
            except Exception as e:
                print("Error updating cart" ,e)
                flash("Error updating cart", "danger")
        else:
            # assuming delete
            try:
                result = DB.delete("DELETE FROM IS601_Cart where product_id = %s and user_id = %s", id, user_id)
                if result.status:
                    flash("Deleted product from cart", "success")

            except Exception as e:
                print("Error deleting product", e)
                flash("Error deleting product from cart", "danger")
    rows = []
    try:
        result = DB.selectAll("""SELECT c.id, product_id, name, c.quantity, (c.quantity * c.cost) as subtotal, i.image
        FROM IS601_Cart c JOIN IS601_Products i on c.product_id = i.id
        WHERE c.user_id = %s
    """, current_user.get_id())

        if result and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error getting cart", e)
        flash("Error fetching cart", "danger")
    return render_template("cart.html", rows=rows)

#adding ability for a user to be able to click on a product on the products page 
#and be sent to an individual product page
#gnb5 4/18/23
@shop.route("/product/<int:product_id>", methods=["GET"])
def product_page(product_id):
    try:
        result = DB.selectOne("SELECT id, name, description, stock, cost, image FROM IS601_Products WHERE id = %s", product_id)
        if result.status and result.row:
            product = result.row
            return render_template("product_page.html", product=product)
        else:
            flash("Product not found", "danger")
            return redirect(url_for("shop.shop_list"))
    except Exception as e:
        print("Error fetching product", e)
        flash("There was a problem loading the product", "danger")
        return redirect(url_for("shop.shop_list"))
    
#clear cart 
@shop.route('/shop/clear_cart', methods=['POST'])
@login_required
def clear_cart():
    user_id = current_user.id

    try:
        result = DB.delete("DELETE FROM IS601_Cart WHERE user_id = %s", user_id)
        if result.status:
            flash("Cart cleared successfully", "success")
    except Exception as e:
        print("Error clearing cart", e)
        flash("Error clearing cart", "danger")

    return redirect(url_for('shop.cart'))


#gnb5 implemented 5/4 conform order page
@shop.route('/confirm_order/<int:order_id>', methods=['GET'])
@login_required
def confirm_order(order_id):
    # Retrieve the order and related order items from the database
    order_result = DB.selectOne("SELECT * FROM IS601_Orders WHERE id = %s", order_id)
    if not order_result.status:
        flash("Error", "danger")
        return False

    order = order_result.row
    #Need to use a join to display names on confirmation page 

    order_items_result = DB.selectAll("""SELECT io.*, p.name
                                    FROM IS601_OrderItems io
                                    JOIN IS601_Products p ON io.product_id = p.id
                                    WHERE io.order_id = %s
                                """, order_id)


    if not order_items_result.status:
        flash("Error", "danger")
        return False

    order_items = order_items_result.rows

    # Calculate the total value
    total_value = sum(item['unit_price'] * item['quantity'] for item in order_items)

    # Retrieve the payment method and amount paid
    payment_method = order['payment_method']
    amount_paid = order['money_received']

    return render_template('confirm_order.html', order_id=order_id, order=order, order_items=order_items, total_value=total_value, payment_method=payment_method, amount_paid=amount_paid)



def process_order(form, current_user):
    # Calculate cart items
    def get_cart_items(user_id):
        result = DB.selectAll("""SELECT c.id, c.product_id, p.name, c.quantity, c.cost, p.stock
                            FROM IS601_Cart c
                            JOIN IS601_Products p ON c.product_id = p.id
                            WHERE c.user_id = %s
                        """, user_id)
        if result.status:
            return result.rows
        else:
            return []
    cart_items = get_cart_items(current_user.id)
    total_price = sum(item['cost'] * item['quantity'] for item in cart_items)
    # Verify if the payment is valid
    # implemented by gnb5 5/4/23
    if form.money_received.data < total_price:
        flash("Payment amount is not sufficient. Please try again.", "warning")
        return False

    #flash(cart_items)


    # Verify product price and stock implemented by gnb5 4/23
    for item in cart_items:
        result = DB.selectOne("SELECT cost, stock FROM IS601_Products WHERE id = %s", item['product_id'])
        print(f"Result: {result}")  # Debug print statement
        if result.status and result.row:
            product_cost, product_stock = result.row["cost"], result.row["stock"]
            print(result.row)
            print(f"Product cost: {product_cost}, Cart item cost: {item['cost']}")  # Debug print statement
            if product_cost != item['cost']:
                flash(f"Price for {item['name']} has changed. Please update your cart.", "warning")
                return False

            if product_stock < item['quantity']:
                flash(f"Insufficient stock for {item['name']}. Please update your cart.", "warning")
                return False
        else:
            flash("Error fetching product details. Please try again.", "danger")
            return False

    # Make an entry into the Orders table
    payment_method = form.payment_method.data
    money_received = form.money_received.data
    address = form.address.data + ', ' + form.city.data + ', ' + form.state.data + ', ' + form.zip_code.data
    user_id = current_user.id

    #FIX THIS 
    #result = DB.insertOne("INSERT INTO IS601_Orders (user_id, payment_method, money_received, address) VALUES (%s, %s, %s, %s)", current_user.id, form.payment_method.data, form.money_received.data, form.address.data)
    result = DB.insertOne("INSERT INTO IS601_Orders (user_id, payment_method, money_received, address, total_price) VALUES (%s, %s, %s, %s, %s)", current_user.id, form.payment_method.data, form.money_received.data, address, total_price)


    if not result.status:
        flash("Error creating order. Please try again.", "danger")
        return False

    # Get last Order ID from Orders table
    #order_id = result.lastrowid
    if result.status:
        # Fetch the primary key of the inserted row
        primary_key_query = "SELECT LAST_INSERT_ID();"
        primary_key_result = DB.selectAll(primary_key_query)

        if primary_key_result.status:
            print("Primary key result rows: ", primary_key_result.rows)
            #inserted_primary_key = primary_key_result.rows[0][0]
            inserted_primary_key = primary_key_result.rows[0]['LAST_INSERT_ID()']
            print( inserted_primary_key)
        else:
            # Handle the error while fetching the primary key
            print("Error fetching primary key")
    else:
    # Handle the error while inserting the row
        print("Error inserting row")

    # Copy the cart details into the OrderItems table with the Order ID from the previous step
    for item in cart_items:
        result = DB.insertOne("INSERT INTO IS601_OrderItems (order_id, product_id, quantity, unit_price) VALUES (%s, %s, %s, %s)",
                        *(inserted_primary_key, item['product_id'], item['quantity'], item['cost']))
        
        if not result.status:
            flash("Error adding order items. Please try again.", "danger")
            return False

        # Update the Products table stock for each item to deduct the ordered quantity
        result = DB.update("UPDATE IS601_Products SET stock = stock - %s WHERE id = %s", *(item['quantity'], item['product_id']))

        if not result.status:
            flash("Error updating product stock. Please try again.", "danger")
            return False
    

    # Clear out the user's cart after successful order
    result = DB.delete("DELETE FROM IS601_Cart WHERE user_id = %s", user_id)

    if not result.status:
        flash("Error clearing cart. Please try again.", "danger")
        return False

    # return for redirect in checkout route
    return inserted_primary_key



#gnb5 implemented 4/23 checkout
@shop.route('/shop/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    
    def get_cart_items(user_id):
        result = DB.selectAll("""SELECT c.id, c.product_id, p.name, c.quantity, c.cost, p.stock
                            FROM IS601_Cart c
                            JOIN IS601_Products p ON c.product_id = p.id
                            WHERE c.user_id = %s
                        """, user_id)
        if result.status:
            return result.rows
        else:
            return []
        
    # Calculate the total amount here
    # Calculate cart items
    cart_items = get_cart_items(current_user.id)
    total_amount= sum(item['cost'] * item['quantity'] for item in cart_items)
    form = CheckoutForm()
    if form.validate_on_submit():
        # Process the form data and create an order in the database
        # still need to implement this function
        success = process_order(form, current_user)
        if success:
            flash("Order successfully placed!", "success")
            return redirect(url_for("shop.confirm_order", order_id=success))
        else:
            flash("Payment failed. Please try again.", "danger")

    #return render_template('checkout.html', form=form)
    #return render_template('checkout.html', form=form, total_amount=total_amount) #adding total of cart
    return render_template('checkout.html', form=form, cart_items=cart_items, total_amount=total_amount)


