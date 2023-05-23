import pandas as pd

def methode():
    # Get Database
    df = pd.read_csv('./airbnbprices/amsterdam_weekdays.csv')

    # Add database to rows list
    rows = []
    for index, row in df.iterrows():
        data = row.to_json()
        rows.append(data)

    # Return this list as JSON
    print(rows[0])
    return rows

def get_city(city, period):
    df = pd.read_csv(f'./airbnbprices/{city}_{period}.csv')
    return df

methode()