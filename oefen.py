import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

totalprice = 0
counter = 0
avprices = []

workDir = './airbnbprices'
for file in os.listdir(workDir): 
    data = pd.read_csv(os.path.join(workDir, file))

    for r,rij in data.iterrows(): # wil je alleen rij naam, moet je een tweede argument toevoegen. 
        if rij["room_type"] == "Private room":
            totalprice += rij["realSum"]
            counter += 1
    
    average = totalprice / counter
    avprices.append(average)

plt.hist(x=avprices, bins=10, alpha=0.5, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('City amount')
plt.ylabel('Average Prices')
plt.title('Average Airbnb private room prices per city')
plt.legend()
plt.show()