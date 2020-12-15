from wtforms import Form, IntegerField, SelectField, validators
from math import pi

class InputForm(Form):
    style = {"style": "text-align:center"}
    decimalPlaces = SelectField(
        label='Select Decimal Approximation:', default=1,
        validators=[validators.InputRequired()],
        choices=[(1, 1), (2, 2), (3, 3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), (10,10)], render_kw=style
        )
    speed = SelectField(label="Select Approximation Speed:", validators=[validators.InputRequired()],
                        choices=[('Slow', 'Slow'), ('Fast', 'Fast')],
                        )