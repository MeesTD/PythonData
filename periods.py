import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector

# Call this function in Flask to get data

def getperiod(year, month):

    # verbinding maken met myphpadmin macbook gegevens
    dbverbinding = mysql.connector.connect(
        host='localhost',
        port='8889',
        user='root',
        password='root',
        database='hotel_booking'
    )
    mijncursor = dbverbinding.cursor()

    mijncursor.execute(f"SELECT * FROM hotel_booking WHERE arrival_date_year = {year} AND arrival_date_month = {month}")

    mydata = mijncursor.fetchall()

    counter = 0
    mealcounter = 0

    for data in mydata:
        counter += 1
        if mydata[3] == "BB":
            mealcounter += 1

    return(f"In {month} {year} there were {counter} bookings. With {str(mealcounter)} getting breakfast.")


getperiod(2015, "July")