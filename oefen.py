import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

def teller(jaar, maand): # de twee gegeven argumenten
    counter = 0

    workDir = './csv_bestanden' # pathway naar gewenste map
    data = pd.read_csv(os.path.join(workDir, 'hotel_bookings.csv')) 
    for r,rij in data.iterrows(): 
        if rij["hotel"] == "City Hotel" and rij["arrival_date_year"] == jaar and rij["arrival_date_month"] == maand : #bij 2016 moet argument jaar, en bij January argument maand
            counter += 1

    return counter