from flask import Flask, render_template, request
from PiCalc import compute
from model import InputForm
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/picalc')
def picalc():
    return render_template('PiCalc.html')

@app.route("/computeResult", methods=['GET', 'POST'])
def computeResult():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result= compute(form.decimalPlaces.data, form.speed.data)
    else:
        result = None
    return render_template("PiCalc.html", form=form, result=result)
if __name__ == '__main__':
   app.run(debug=True)