from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, TextAreaField, IntegerField, URLField, SubmitField, BooleanField, FloatField, SelectField
from wtforms.validators import DataRequired, Length, Optional, NumberRange, InputRequired, ValidationError
import re

class ProductForm(FlaskForm):
    id = HiddenField("id", validators=[Optional()])
    name = StringField("name", validators=[DataRequired(), Length(max=30)])
    description = TextAreaField("description", validators=[DataRequired()])
    stock = IntegerField("stock", validators=[NumberRange(min=0)])
    cost = IntegerField("cost", validators=[NumberRange(min=0)])
    image = URLField("image", validators=[Optional()])
    submit = SubmitField("Save")
    category = StringField('category')  # Add this line
    visibility = BooleanField('visibility')  # Add this line

#https://www.w3schools.com/python/python_regex.asp
def validate_address_pieces(form, field):
    # Assuming a valid US address
    address_regex = re.compile(r'^\d{1,5}\s([A-Za-z]+\s)+\w+,\s\w{2},\s\d{5}$')
    if not address_regex.match(field.data):
        raise ValidationError("Invalid address format. Example: '1234 Main St, CA, 90210'")

class CheckoutForm(FlaskForm):
    payment_method = SelectField("Payment Method", choices=[("Cash", "Cash"), ("Visa", "Visa"), ("MasterCard", "MasterCard"), ("Amex", "Amex")])
    money_received = FloatField("Payment Amount", validators=[InputRequired()])
    address = StringField("Address", validators=[InputRequired(), Length(max=255)])
    city = StringField("City", validators=[InputRequired(), Length(max=100)])
    state = StringField("State", validators=[InputRequired(), Length(max=100)])
    zip_code = StringField("Zip Code", validators=[InputRequired(), Length(max=10)])
    submit = SubmitField("Checkout")

