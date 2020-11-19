from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Funnnciona :)"


@app.route("/barcelonaActiva")
def newEndpoint():
    return "primera app a azure amb backend"


@app.route("/renderingTemplate")
def rendertemplate():
    return render_template('test.html')
