from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
company = Blueprint('company', __name__, url_prefix='/company')

@company.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count as employees for the company
    # don't do SELECT *
    query = """SELECT id, name, address, city, country, state, zip, website,
                (SELECT COUNT(*) FROM IS601_MP3_Employees WHERE company_id = IS601_MP3_Companies.id) as employees
            FROM IS601_MP3_Companies WHERE 1=1"""

    #query = "SELECT id, name, address, city, country, state, zip, website, employee_count as employees FROM IS601_MP3_Companies WHERE 1=1"
    
    args = {} # <--- add values to replace %s/%(named)s placeholders
    #DB.selectAll() method might be expecting a tuple instead of a dictionary for the query parameters
    # Initialize args_list as an empty list instead of an empty dictionary.
    #args_list = []
    
    #allowed_columns = ["name", "city", "country", "state"]
    allowed_columns = ["id", "name", "address", "city", "country", "state", "zip", "website", "employees"]

    # TODO search-2 get name, country, state, column, order, limit request args
    allowed_orders = ["asc", "desc"]
    name = request.args.get('name_company')
    country = request.args.get('country')
    state = request.args.get('state')
    column = request.args.get('column')
    order = request.args.get('order')
    limit = request.args.get('limit', default=10, type=int)
    # limit = 10 # TODO change this per the above requirements

    # TODO search-3 append a LIKE filter for name if provided
    if name:
        query += " AND name LIKE %s"
        args['name'] = f"%{name}%"
    # TODO search-4 append an equality filter for country if provided
    if country:
        query += " AND country = %s"
        args['country'] = country
    # TODO search-5 append an equality filter for state if provided
    if state:
        query += " AND state = %s"
        args['state'] = state
    # TODO search-6 append sorting if column and order are provided and within the allows columsn and allowed order asc,desc
    if column and order and column in allowed_columns and order in allowed_orders:
        query += f" ORDER BY {column} {order}"

    # TODO search-7 append limit (default 10) or limit greater than 1 and less than or equal to 100
    if limit < 1 or limit > 100:
        flash("Limit should be between 1 and 100", "danger")
    else:
        query += " LIMIT %s"
        #args_list.append(limit)
        args["limit"] = limit

    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
    print("query",query)
    print("args", args)
    try:
        #result = DB.selectAll(query, *args_list)
        result = DB.selectAll(query, tuple(args.values()))
        if result.status:
            rows = result.rows
            print(f"rows {rows}")
    except Exception as e:
        flash("An error occurred while searching for companies.", "danger")
        # TODO search-9 make message user friendly
        flash(str(e), "danger")

    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    
    #columns_tuples = [(col, col.capitalize()) for col in allowed_columns]
    
    #return render_template("list_companies.html", rows=rows, allowed_columns=columns_tuples)
    return render_template("list_companies.html", rows=rows, allowed_columns=allowed_columns)

@company.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        name = request.form.get("name")
        address = request.form.get("address")
        city = request.form.get("city")
        state = request.form.get("state")
        country = request.form.get("country")
        zip_code = request.form.get("zip")
        print(zip_code)
        website = request.form.get("website")
        # TODO add-2 name is required (flash proper error message)
        if not name:
            flash("Name is required", "danger")
            has_error = True
        # TODO add-3 address is required (flash proper error message)
        if not address:
            flash("Address is required", "danger")
            has_error = True

        # TODO add-4 city is required (flash proper error message)
        if not city:
            flash("City is required", "danger")
            has_error = True
        # TODO add-5 state is required (flash proper error message)
        # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
        # hint see geography.py and pycountry documentation
        if not state:
            flash("State is required", "danger")
            has_error = True
        #else:
            # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
            '''
            if not is_valid_state(state):
                flash("Invalid state", "danger")
                has_error = True
            
            '''

        # TODO add-6 country is required (flash proper error message)
        # TODO add-6a country should be a valid country mentioned in pycountry
        # hint see geography.py and pycountry documentation
        if not country:
            flash("Country is required", "danger")
            has_error = True
        #else:
            # TODO add-6a country should be a valid country mentioned in pycountry
            '''
            if not is_valid_country(country):
                flash("Invalid country", "danger")
                has_error = True
            '''
        # TODO add-7 website is not required
        if not zip_code:
            flash("No website", "danger")
            has_error = False

        # TODO add-8 zipcode is required (flash proper error message)
        if not zip_code:
            flash("Zip code is required", "danger")
            has_error = True
        # note: call zip variable zipcode as zip is a built in function it could lead to issues

        has_error = False # use this to control whether or not an insert occurs
        

        if not has_error:
            try:
                print("Parameters:", (name, address, city, state, country, zip_code, website))
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Companies (name, address, city, state, country, zip, website)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (name, address, city, state, country, zip_code, website))
                
                print("inserted")

                # TODO add-8 add query and add arguments
                if result.status:
                    flash("Added Company", "success")
            except Exception as e:
                # TODO add-9 make message user friendly
                flash(str(e), "danger")

    return render_template("add_company.html")
'''
@company.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    id = False
    if not id: # TODO update this for TODO edit-1
        pass
    else:
        if request.method == "POST":
            data = {"id": id} # use this as needed, can convert to tuple if necessary
            # TODO edit-1 retrieve form data for name, address, city, state, country, zip, website
            # TODO edit-2 name is required (flash proper error message)
            # TODO edit-3 address is required (flash proper error message)
            # TODO edit-4 city is required (flash proper error message)
            # TODO edit-5 state is required (flash proper error message)
            # TODO edit-5a state should be a valid state mentioned in pycountry for the selected state
            # hint see geography.py and pycountry documentation
            # TODO edit-6 country is required (flash proper error message)
            # TODO edit-6a country should be a valid country mentioned in pycountry
            # hint see geography.py and pycountry documentation
            # TODO edit-7 website is not required
            # TODO edit-8 zipcode is required (flash proper error message)
            
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            # populate data dict with mappings
            has_error = False # use this to control whether or not an insert occurs

            
            if not has_error:
                try:
                    # TODO edit-9 fill in proper update query
                    # name, address, city, state, country, zip, website
                    result = DB.update("""
                    UPDATE ...
                    SET
                    ...
                    """, data)
                    if result.status:
                        print("updated record")
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-10 make this user-friendly
                    print(f"{e}")
                    flash(str(e), "danger")
        row = {}
        try:
            # TODO edit-11 fetch the updated data
            result = DB.selectOne("SELECT ... FROM ... WHERE ...", id)
            if result.status:
                row = result.row
                
        except Exception as e:
            # TODO edit-12 make this user-friendly
            flash(str(e), "danger")
    # TODO edit-13 pass the company data to the render template
    return render_template("edit_company.html", ...)
'''
@company.route("/edit", methods=["GET", "POST"])
def edit():
    id = request.args.get('company_id')
    print(id)

    if not id:
        flash("Company ID is required", "danger")
        return redirect(url_for("company.search"))

    if request.method == "POST":
        data = {"id": id}
        form_data = request.form.to_dict()

        has_error = False

        if not form_data.get('name'):
            flash("Name is required", "danger")
            has_error = True
        if not form_data.get('address'):
            flash("Address is required", "danger")
            has_error = True
        if not form_data.get('city'):
            flash("City is required", "danger")
            has_error = True
        if not form_data.get('state'):
            flash("State is required", "danger")
            has_error = True
        if not form_data.get('country'):
            flash("Country is required", "danger")
            has_error = True
        if not form_data.get('zip'):
            flash("Zip code is required", "danger")
            has_error = True

        data.update(form_data)

        if not has_error:
            print("The Data:", data)
            try:
                result = DB.update("""
                UPDATE IS601_MP3_Companies
                SET
                name = %s,
                address = %s,
                city = %s,
                state = %s,
                country = %s,
                zip = %s,
                website = %s
                WHERE id = %s
                """, (form_data.get('name'), form_data.get('address'), form_data.get('city'), form_data.get('state'), form_data.get('country'), form_data.get('zip'), form_data.get('website'), id))
                
                if result.status:
                    flash("Updated record", "success")
                    return redirect(url_for("company.search"))
            except Exception as e:
                print("Exception is:", e)
                flash("An error occurred while updating the company", "danger")

    row = {}
    try:
        result = DB.selectOne("SELECT * FROM IS601_MP3_Companies WHERE id = %s", (id,))
        if result.status:
            row = result.row
    except Exception as e:
        print(e)
        flash("An error occurred while retrieving the company", "danger")

    return render_template("edit_company.html", row=row)



@company.route("/delete", methods=["GET"])
def delete():
    # gnb5 implemented 4/7/23
    # TODO delete-6 if id is missing, flash necessary message and redirect to search
    company_id = request.args.get("company_id")
    print("C_id is:", company_id)

    if company_id is None:
        flash("Company ID is required", "danger")
        return redirect(url_for("company.search"))
    
    try:
        # Unassign employees from the company
        # TODO delete-5 for all employees assigned to this company set their company_id to None/null
        update_employees_query = """
        UPDATE IS601_MP3_Employees SET company_id = NULL WHERE company_id = %s
        """
        update_result = DB.update(update_employees_query, (company_id,))

        # TODO delete-1 delete company by id (unallocate any employees see delete-5)
        # TODO delete-3 pass all argument except id to this route
        # Delete the company
        delete_query = """
        DELETE FROM IS601_MP3_Companies WHERE id = %s
        """
        delete_result = DB.delete(delete_query, (company_id,))
        if delete_result.status:
            # TODO delete-4 ensure a flash message shows for successful delete
            flash("Company and related data were successfully deleted", "success")
        else:
            flash("An error occurred while deleting the company", "danger")

    except Exception as e:
        flash("An error occurred while deleting the company", "danger")

    # TODO delete-2 redirect to company search
    return redirect(url_for("company.search"))
