from flask import jsonify
import os
import mysql.connector
import windowsgebruik

# Call this function in Flask to get data

# verbinding maken met myphpadmin macbook gegevens
# LET OP: Navisa & Mees hebben Macs, dus password is anders
dbverbinding = mysql.connector.connect(
    host=windowsgebruik.krijgservernaam(),
    port=windowsgebruik.krijgpoort(),
    user=windowsgebruik.krijguser(),
    password=windowsgebruik.krijgwachtwoord(),
    database='hotel_booking'
)
mijncursor = dbverbinding.cursor()

def getperiod(year, month, day):
    print("Verzoek aan getperiod functie voor de dag")
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
        price += int(data[13])
        counter += 1
        if data[12] == 'BB':
            mealcounter += 1

    pricecal = price/counter

    return jsonify(date = year + ' ' + month + ' ' + day, reservations = counter, breakfast = mealcounter, price = pricecal)


def getperiod_month(year, month):
    print("Verzoek aan getperiod_month functie voor de maand")
    # Create a variable to hold the SQL statement and fill it with relevant variables
    sql_check_data = 'SELECT * FROM hotel_booking WHERE arrival_date_year = %s AND arrival_date_month = %s'
    mijncursor.execute(sql_check_data, (year, month))
    mydata = mijncursor.fetchall()

    # pakt voor elke rij de juiste waarden van jaar, maand en maaltijd en kosten uit de dataset
    months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

    keys = [i[0] for i in mijncursor.description]

    data = [
        dict(zip(keys, row)) for row in mydata
    ]
    return data
