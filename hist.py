import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np


booking = {}

workDir = './csv_bestanden/hotel_bookings.csv' # pathway naar gewenste map
for file in os.listdir(workDir):
    data = pd.read_csv(os.path.join(workDir, file)) 
    for r,rij in data.iterrows(): 
        if rij["room_type"] == "Private room":
            if file[0:3] not in booking:
                booking[file[0:3]] = 0
            booking[file[0:3]] += 1

city = list(booking.keys())
values = list(booking.values())

plt.bar(range(len(booking)), values, tick_label=city)
plt.xlabel('City')
plt.ylabel('Visitors')
plt.title('Visitors per city')
plt.legend()
plt.show()

"""
booking = {}

workDir = './csv_bestanden' # pathway naar gewenste map
data = pd.read_csv(os.path.join(workDir, 'hotel_bookings.csv')) 
for r,rij in data.iterrows(): 
    if rij["hotel"] == "City Hotel" and rij["arrival_date_year"] == 2016:
        if rij["arrival_date_month"] not in booking:
            booking[rij["arrival_date_month"]] = 0
        booking[rij["arrival_date_month"]] += 1

months = list(booking.keys())
values = list(booking.values())

plt.bar(range(len(booking)), values, tick_label=months)
plt.xlabel('Months')
plt.ylabel('Visitors')
plt.title('Visitors per month 2016')
plt.legend()
plt.show()
"""
