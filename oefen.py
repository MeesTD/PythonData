from flask import jsonify
import os
import mysql.connector
import windowsgebruik
import functools

dbverbinding = mysql.connector.connect(
    host='localhost',
    port=windowsgebruik.krijgpoort(),
    user='root',
    password=windowsgebruik.krijgwachtwoord(),
    database='hotel_booking'
)

mijncursor = dbverbinding.cursor()

    # Create a variable to hold the SQL statement and fill it with relevant variables
sql_check_data = 'SELECT * FROM hotel_booking'
mijncursor.execute(sql_check_data) # execute(SQL statement, (hier de waarden voor de plekken %s en op volgorde)

mydata = mijncursor.fetchall()

prijs = 250
teller = 0

for data in mydata:
    res = data[6]
    prijs += res
    teller += 1

roomprijs = prijs / teller

print(roomprijs)