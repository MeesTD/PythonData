from flask import jsonify
import os
import mysql.connector
import windowsgebruik

# Call this function in Flask to get data

# verbinding maken met myphpadmin macbook gegevens
# LET OP: Navisa & Mees hebben Macs, dus password is anders
dbverbinding = mysql.connector.connect(
    host='localhost',
    port=windowsgebruik.krijgpoort(),
    user='root',
    password=windowsgebruik.krijgwachtwoord(),
    database='hotel_booking'
)
mijncursor = dbverbinding.cursor()

def methode():
    print("Hier is Rhea")
    return "ABC"

def methode2(da, db):
    dbverbinding = mysql.connector.connect(
        host=windowsgebruik.krijgservernaam(),
        port=windowsgebruik.krijgpoort(),
        user=windowsgebruik.krijguser(),
        password=windowsgebruik.krijgwachtwoord(),
        database='hotel_booking'
    )
    mijncursor = dbverbinding.cursor()
    sql_check_data = "SELECT date, SUM(adults) AS adults, SUM(children) AS children, SUM(babies) AS babies FROM `hotel_booking` WHERE date >= '"+da+"' AND date <= '"+db+"' GROUP BY date ;"
    mijncursor.execute(sql_check_data) # execute(SQL statement, (hier de waarden voor de plekken %s en op volgorde)
    mydata = mijncursor.fetchall()

    keys = [i[0] for i in mijncursor.description]

    data = [
        dict(zip(keys, row)) for row in mydata
    ]
    return data
