from flask import jsonify
import os
import mysql.connector
import windowsgebruik
from datetime import date, timedelta, datetime
import calendar

# This method returns True if a customer paid less than avg
# And false if a customer paid more than avg
def price_check(start, end, paid):

    # Call this function in Flask to get data
    sdate = datetime.date(datetime.strptime(start , "%Y-%m-%d"))
    edate = datetime.date(datetime.strptime(end , "%Y-%m-%d"))
    dates = []
    pricebooking = 0

    delta = timedelta(days=1)

    while sdate <= edate:
        dates.append(sdate.isoformat())
        sdate += delta

    dbverbinding = mysql.connector.connect(
        host=windowsgebruik.krijgservernaam(),
        port=windowsgebruik.krijgpoort(),
        user=windowsgebruik.krijguser(),
        password=windowsgebruik.krijgwachtwoord(),
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
        price = 0

    # Loop over the fetched data and start counting relevant database entries
        for data in mydata:
            price += int(data[13])
            counter += 1
            if data[5] == 'BB':
                mealcounter += 1

        pricecal = price/counter
        pricebooking += pricecal

    # Compare adr of data to adr of paid amount
    booking = pricebooking/len(dates)
    paid_adr = int(paid)/len(dates)
    difference = booking - paid_adr
    if difference >= 0:
        return "true"
    elif difference < 0:
        return "false"