from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/picalc')
def picalc():
    return render_template('PiCalc.html')

@app.route("/speed", methods=['POST'])
def speed():
    speed=request.form["speeds"]
    return render_template('PiCalc.html', selectedSpeed=speed)
if __name__ == '__main__':
   app.run()