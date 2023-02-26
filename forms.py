from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class BudgetForm(FlaskForm):
    pozycja = StringField("pozycja", validators=[DataRequired()])
    opis = TextAreaField("opis", validators=[DataRequired()])
    payment_status = BooleanField("payment_status", validators=[DataRequired()])