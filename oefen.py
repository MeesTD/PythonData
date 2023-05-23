import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

totalprice = 0
counter = 0
yplot = []
xplot = []

workDir = './airbnbprices' # pathway naar gewenste map

for file in sorted(os.listdir(workDir)): # geef alle files in map
    data = pd.read_csv(os.path.join(workDir, file)) # open alle files in map
    name = os.path.splitext(file)[0][:3] # aanpassing

    for r,rij in data.iterrows(): # wil je alleen rij naam, moet je een tweede argument toevoegen. 
        if rij["room_type"] == "Private room":
            totalprice += rij["realSum"]
            counter += 1
    
    
    average = totalprice / counter
    yplot.append(average)
    xplot.append(name)
    lab_x = [i for i in range(len(xplot))]

plt.bar(lab_x, yplot)
plt.xticks(lab_x, xplot)
plt.xlabel('City')
plt.ylabel('Average Prices')
plt.title('Average Airbnb private room prices per city')
plt.legend()
plt.show()