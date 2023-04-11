from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
import re
employee = Blueprint('employee', __name__, url_prefix='/employee')


@employee.route("/search", methods=["GET"])
def search():
    rows = []
    # gnb5 added 4/9/23
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    query = """SELECT employees.id, employees.first_name, employees.last_name, employees.email, companies.id as company_id, companies.name as company_name
    FROM IS601_MP3_Employees AS employees LEFT JOIN IS601_MP3_Companies AS companies ON employees.company_id = companies.id WHERE 1=1"""
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["first_name", "last_name", "email", "company_name"]
    #print("the query result",query)

    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    # gnb5 added 4/9/23
    fn = request.args.get("fn")
    #print("first name is:",fn)
    ln = request.args.get("ln")
    email = request.args.get("email")
    company = request.args.get("company")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10, type=int)

    # gnb5 added 4/9/23
    # TODO search-3 append like filter for first_name if provided
    if fn:
        query += " AND employees.first_name LIKE %s"
        args["fn"] = f"%{fn}%"

    # TODO search-4 append like filter for last_name if provided
    if ln:
        query += " AND employees.last_name LIKE %s"
        args["ln"] = f"%{ln}%"


    # TODO search-5 append like filter for email if provided
    if email:
        query += " AND employees.email LIKE %s"
        args["email"] = f"%{email}%"

    # TODO search-6 append equality filter for company_id if provided
    if company:
        query += " AND employees.company_id = %s"
        args["company"] = company

    # gnb5 added 4/9/23
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    if column in allowed_columns and order in ["asc", "desc"]:
        query += f" ORDER BY {column} {order}"

    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
    # gnb5 added 4/9/23
    try:
        limit = int(limit)
        if limit < 1 or limit > 100:
            flash("Invalid limit value. Please enter a number between 1 and 100.", "warning")
            raise ValueError     
    except (TypeError, ValueError):
        limit = 10
        flash("Limit should be a number between 1 and 100. Using default limit of 10.", "warning")
        
    # gnb5 added 4/9/23
    #limit = 10 # TODO change this per the above requirements
    query += " LIMIT %s"
    args["limit"] = limit
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, tuple(args.values()))
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-10 make message user friendly
        flash(e, "An error occurred while processing your request. Please try again.")

    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    allowed_columns_tuples = [(col, col.replace("_", " ").title()) for col in allowed_columns]

    return render_template("list_employees.html", rows=rows, allowed_columns=allowed_columns_tuples)
    #return redirect(url_for('employee.search'))


@employee.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # gnb5 added 4/9/23
        # TODO add-1 retrieve form data for first_name, last_name, company, email

        first_name = request.form.get("first_name", "").strip()
        #print(first_name)
        last_name = request.form.get("last_name", "").strip()
        #print(last_name)
        company = request.form.get("company", "").strip()
        #print("company",company)
        email = request.form.get("email", "").strip()
        #print(email)

        # gnb5 added 4/9/23
        # TODO add-2 first_name is required (flash proper error message)
        # TODO add-3 last_name is required (flash proper error message)
        # TODO add-4 company (may be None)
        # TODO add-5 email is required (flash proper error message)
        has_error = False
        if not first_name:
            flash("First name is required", "error")
            has_error = True
        if not last_name:
            flash("Last name is required", "error")
            has_error = True
        if not email:
            flash("Email is required", "error")
            has_error = True
        else:
            # TODO add-5a verify email is in the correct format
            import re
            email_regex = r"[^@]+@[^@]+\.[^@]+"
            #print("valid email")
            if not re.match(email_regex, email):
                flash("Invalid email format", "error")
                has_error = True

        if not has_error:
            try:
                # TODO add-6 add query and add arguments
                print("Before updating...")  # Add this line
                print("parameters:", first_name, last_name, email, company, id)
                print("Parameters:", (first_name, last_name, company, email))

                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Employees (first_name, last_name, email, company_id)
                VALUES (%s, %s, %s, %s)
                """, (first_name, last_name, email, company))

                if result.status:
                    flash("Created Employee Record", "success")
                    #return redirect(url_for('employee.list'))  # Redirect to the employee list page
                    return redirect(url_for('employee.search'))  # Redirect to the employee list page

            except Exception as e:
                # TODO add-7 make message user friendly
                flash("Error: Could not create employee record. Please try again.", "danger")
                print(f"Exception: {e}")  # Add this line to print the exception
    return render_template("add_employee.html")

@employee.route("/edit", methods=["GET", "POST"])
def edit():
    # gnb5 added 4/9/23
    # TODO edit-1 request args id is required (flash proper error message)
    id = request.args.get("id", None)
    #print({id})
    if not id:
        flash("Employee ID is required.", "danger")
        # TODO fix this possibly
        return redirect(url_for("employee.search"))
    
    else:
        if request.method == "POST":
            # gnb5 added 4/9/23
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            first_name = request.form.get("first_name", "").strip()
            print(first_name)
            last_name = request.form.get("last_name", "").strip()
            print(last_name)
            company = request.form.get("company", "").strip()
            print("company",company)
            email = request.form.get("email", "").strip()
            print(email)
            # gnb5 added 4/9/23
            # TODO edit-2 first_name is required (flash proper error message)
            # TODO edit-3 last_name is required (flash proper error message)
            # TODO edit-4 company (may be None)
            # TODO edit-5 email is required (flash proper error message)
            # TODO edit-5a verify email is in the correct format
            has_error = False # use this to control whether or not an insert occurs
            if not first_name:
                flash("First name is required.", "danger")
                has_error = True
            if not last_name:
                flash("Last name is required.", "danger")
                has_error = True
            if not email:
                flash("Email is required.", "danger")
                has_error = True
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                flash("Email format is invalid.", "danger")
                has_error = True
            
            if not has_error:
                try:
                    # gnb5 added 4/9/23
                    # TODO edit-6 fill in proper update query
                    #print("Before updating...")  # Add this line
                    #print("parameters:", first_name, last_name, email, company, id)

                    result = DB.update("""
                    UPDATE IS601_MP3_Employees SET
                    first_name=%s, last_name=%s, email=%s, company_id=%s
                    WHERE id=%s
                    """, (first_name, last_name, email, company, id))

                    #print("After updating...")  # Add this line
                    #print(f"Update result: {result}")  # Add this line
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-7 make this user-friendly
                    print(f"Exception: {e}")  # Add this line to print the exception
                    flash("Error updating record. Please try again.", "danger")

        row = {}
        try:
            # gnb5 added 4/9/23
            # TODO edit-8 fetch the updated data 
            result = DB.selectOne("""
            SELECT e.id, e.first_name, e.last_name, e.email, e.company_id as company
            FROM IS601_MP3_Employees e
            WHERE e.id = %s
            """, (id,))
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-9 make this user-friendly
            flash("Error fetching employee data. Please try again.", "danger")
    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html", employee=row)
    

@employee.route("/delete", methods=["GET"])
def delete():
    employee_id = request.args.get("id")
    print("E_id is:",employee_id)
    # gnb5 added 4/9/23
    # TODO delete-5 if id is missing, flash necessary message and redirect to search
    if not employee_id:
        flash("Employee ID is missing. Please provide a valid employee ID.", "warning")
        return redirect(url_for("employee.search"))
    try:
        # TODO delete-1 delete employee by id
        query = "DELETE FROM IS601_MP3_Employees WHERE id = %s"
        print("DELETE QUERY:",query)
        #result = DB.execute(query, {"id": employee_id})
        result = DB.delete(query, (employee_id,))


        if result.status:
            # TODO delete-4 ensure a flash message shows for successful delete
            flash("Employee successfully deleted.", "success")
        else:
            flash("An error occurred while deleting the employee. Please try again.", "error")
    except Exception as e:
        flash("An error occurred while processing your request. Please try again.", "error")
        print(f"Exception details: {e}")
    
    # TODO delete-3 pass all argument except id to this route
    redirect_args = {key: value for key, value in request.args.items() if key != "id"}

    # TODO delete-2 redirect to employee search
    return redirect(url_for("employee.search", **redirect_args))

