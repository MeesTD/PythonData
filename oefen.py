from flask import jsonify
import os
import mysql.connector
import windowsgebruik
from datetime import date, timedelta, datetime
import calendar

# Call this function in Flask to get data
sdate = date(2023, 3, 22)
edate = date(2023, 4, 1)
dates = []
pricebooking = 0

delta = timedelta(days=1)

while sdate <= edate:
    dates.append(sdate.isoformat())
    sdate += delta

dbverbinding = mysql.connector.connect(
        host='localhost',
        port=8889,
        user='root',
        password='root',
        database='hotel_booking'
    )

mijncursor = dbverbinding.cursor()

for date in dates:
    dt = datetime.strptime(date, '%Y-%m-%d')
    month = calendar.month_name[dt.month]
    # Create a variable to hold the SQL statement and fill it with relevant variables
    sql_check_data = 'SELECT * FROM hotel_booking WHERE arrival_date_month = %s AND arrival_date_day_of_month = %s'
    mijncursor.execute(sql_check_data, (month, dt.day)) # execute(SQL statement, (hier de waarden voor de plekken %s en op volgorde)

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
    pricebooking += pricecal

booking = pricebooking/len(dates)
print(booking)