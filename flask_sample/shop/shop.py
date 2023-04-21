from flask import Blueprint, request, flash, render_template, redirect, url_for
from werkzeug.datastructures import MultiDict
from shop.forms import ProductForm
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

'''
@shop.route("/shop", methods=["GET","POST"])
def shop_list():
    rows = []
    try:
        result = DB.selectAll("SELECT id, name, description, stock, cost, image, visibility FROM IS601_Products WHERE stock > 0 LIMIT 10",)
        #george: rows = db.session.query(Product).order_by(Product.created_at.desc()).limit(10).all()
        if result.status and result.rows:
            rows = result.rows
            print(result.rows[1])
            #need to only show product if visible =0
    except Exception as e:
        print("Error fetching products", e)
        flash("There was a problem loading products", "danger")
    return render_template("shop.html", rows=rows)
'''
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
