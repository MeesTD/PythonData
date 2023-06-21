from flask import Flask
import mees as mees
import felixbestand
import rhea
import navisa
#import periods
import periods_rhea
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/mees")
def mees1():
    return mees.show()

@app.route("/mees2/<datuma>/<datumb>")
def mees2(datuma, datumb):
    return mees.plot(datuma, datumb)

@app.route("/felix")
def felixmethode():
    return felixbestand.methode()

@app.route("/rhea")
def rheaethode():
    return rhea.methode()

@app.route("/navisa")
def navisa2():
    return navisa.methode()

# User enters period, gets amount of reservations in given period as string
# MIND THAT our database starts in July 2015 and ends at August 2017

@app.route("/getperiod/<year>/<month>/<day>")
def getday(year, month, day):
    return periods_rhea.getperiod(year, month, day)

@app.route("/getperiod/<year>/<month>")
def getmonth(year, month):
    return periods_rhea.getperiod_month(year, month)

# Eventueel optie voor resort/city hotels.
# 
