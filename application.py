from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Funnnciona :)"


@app.route("/barcelonaActiva")
def hello():
    return "primera app a azure amb backend"
