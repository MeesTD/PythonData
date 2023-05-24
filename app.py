from flask import Flask
import mees
import felixbestand
import rhea
import navisa
import periods

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/mees")
def mees2():
    return mees.methode()

@app.route("/felix")
def felixmethode():
    return felixbestand.methode()

@app.route("/rhea")
def rheaethode():
    return rhea.methode()

@app.route("/navisa")
def navisa2():
    return navisa.methode()

@app.route("/<periode>")
def getcity(period):
    return periods.getyear(period)

# Eventueel optie voor resort/city hotels

