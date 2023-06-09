from flask import jsonify
import os
import mysql.connector
import windowsgebruik

# Call this function in Flask to get data

def getperiod(year, month, day):

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

    # Create a variable to hold the SQL statement and fill it with relevant variables
    sql_check_data = 'SELECT * FROM hotel_booking WHERE arrival_date_year = %s AND arrival_date_month = %s AND arrival_date_day_of_month = %s'
    mijncursor.execute(sql_check_data, (year, month, day)) # execute(SQL statement, (hier de waarden voor de plekken %s en op volgorde)

    mydata = mijncursor.fetchall()

    
    # Create the counters and start counting in the SQL table
    counter = 0
    mealcounter = 0
    price = 0

    # Loop over the fetched data and start counting relevant database entries
    for data in mydata:
        price += int(data[6])
        counter += 1
        if data[5] == 'BB':
            mealcounter += 1

    pricecal = price/counter
    
    return jsonify(date = year + ' ' + month + ' ' + day, reservations = counter, breakfast = mealcounter, price = pricecal)