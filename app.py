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

# User enters period, gets amount of reservations in given period as string
# MIND THAT our database starts in July 2015 and ends at August 2017

@app.route("/getperiod/<year>/<month>/<day>")
def getmonth(year, month, day):
    return periods.getperiod(year, month, day)



# Eventueel optie voor resort/city hotels.
# 
