import pandas as pd

#def methode():
    # Get Database
   # df = pd.read_csv('./airbnbprices/amsterdam_weekdays.csv')

    # Add database to rows list
   # rows = []
    #for index, row in df.iterrows():
    #    data = row.to_json()
       # rows.append(data)

    # Return this list as JSON
   # return rows

# Naam CSV

# Op basis van DD/MM/JJJJ 
# Hoeveelheid bezoekers returnen


# Deze ten opzichte van andere maaanden



# Dit is een oude functie verstrengeld met de nieuwe
# HERSCHRIJVEN

def getyear(year):
    df = pd.read_csv(f'./airbnbprices/{city}_{period}.csv')
    # Add database to rows list
    rows = []
    for index, row in df.iterrows():
        data = row.to_json()
        rows.append(data)

    return rows