import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

# Call this function in Flask to get data

def getperiod(year, month):
    counter = 0
    mealcounter = 0
    year = int(year) #TODO Returns error if year is not int
    month = str(month)
    workDir = './csv_bestanden' # pathway naar gewenste map

    data = pd.read_csv(os.path.join(workDir, 'hotel_bookings.csv')) 
    
    # Count the amount of bookings in given period + meals.
    for r,rij in data.iterrows(): 
        if rij["hotel"] == "City Hotel" and rij["arrival_date_year"] == year and rij["arrival_date_month"] == month : #bij 2016 moet argument jaar, en bij January argument maand
            counter += 1
            if rij['meal'] == 'BB':
                mealcounter += 1
    
    # Returns string. May need to be changed for Java implementation.
    # Returns 0 if dates don't exist in database. 

    return(f"In {month} {year} there were {counter} bookings. With {str(mealcounter)} getting breakfast.")


getperiod(2015, "July")