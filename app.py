from flask import Flask, render_template, request
from PiCalc import compute
from PiCalc import PiCalc
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
        obj = PiCalc(int(form.decimalPlaces.data))
        numTerms = 0
        approximation = 0
        if (form.speed.data == "Fast"):
            numTerms = obj.getNumberTermsMachinApprox()
            print(numTerms)
            approximation = obj.fast_pi_approximation()
            print(approximation)
        else:
            numTerms = obj.getNumberTermsSlowApprox()
            print(numTerms)
            approximation = obj.calculation_slow_approx()
            print(approximation)
    else:
        result = None
    return render_template("PiCalc.html", form=form, result=result, numTerms=numTerms, approximation=approximation)

@app.route("/stockMarketScraper")
def stockScraper():
    return render_template("StockScraper.html")
if __name__ == '__main__':
   app.run(debug=True)