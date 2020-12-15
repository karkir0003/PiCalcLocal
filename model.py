from wtforms import Form, IntegerField, SelectField, validators
from math import pi

class InputForm(Form):
    decimalPlaces = SelectField(
        label='number of decimal places', default=1,
        validators=[validators.InputRequired()],
        choices=[(1, 1), (2, 2), (3, 3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), (10,10)]
        )
    speed = SelectField(label="Speed", validators=[validators.InputRequired()],
                        choices=[('Slow', 'slow'), ('Fast', 'fast')],
                        )