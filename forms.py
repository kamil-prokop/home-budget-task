from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class BudgetForm(FlaskForm):
    position = StringField('pozycja', validators=[DataRequired()])
    description = TextAreaField("opis", validators=[DataRequired()])
    payment_status = BooleanField("zapłacone", validators=[DataRequired()])