from flask import jsonify
import os
import mysql.connector
import windowsgebruik

# Call this function in Flask to get data

# verbinding maken met myphpadmin macbook gegevens
# LET OP: Navisa & Mees hebben Macs, dus password is anders
dbverbinding = mysql.connector.connect(
    host='localhost',
    port=windowsgebruik.krijgpoort(),
    user='root',
    password=windowsgebruik.krijgwachtwoord(),
    database='hotel_booking'
)
mijncursor = dbverbinding.cursor()

def getperiod(year, month, day):
    print("Verzoek aan getperiod functie voor de dag")
    # Create a variable to hold the SQL statement and fill it with relevant variables
    sql_check_data = 'SELECT * FROM hotel_booking WHERE arrival_date_year = %s AND arrival_date_month = %s AND arrival_date_day_of_month = %s'
    mijncursor.execute(sql_check_data, (year, month, day)) # execute(SQL statement, (hier de waarden voor de plekken %s en op volgorde)
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

    return jsonify(date = year + ' ' + month + ' ' + day, reservations = counter, breakfast = mealcounter, price = pricecal)


def getperiod_month(year, month):
    print("Verzoek aan getperiod_month functie voor de maand")
    # Create a variable to hold the SQL statement and fill it with relevant variables
    sql_check_data = 'SELECT * FROM hotel_booking WHERE arrival_date_year = %s AND arrival_date_month = %s'
    mijncursor.execute(sql_check_data, (year, month)) # execute(SQL statement, (hier de waarden voor de plekken %s en op volgorde)
    mydata = mijncursor.fetchall()

    # pakt voor elke rij de juiste waarden van jaar, maand en maaltijd en kosten uit de dataset
    months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

    id = mydata[0]
    hotel = mydata[1]
    is_canceled = mydata[2]
    lead_time = mydata[3]
    arrival_date_year = mydata[4]
    arrival_date_month = mydata[5]
    arrival_date_day_of_month = mydata[6]
    stays_in_weekend_nights = mydata[7]
    stays_in_week_nights =  mydata[8]
    adults =  mydata[9]
    children = mydata[10]
    babies = mydata[11]
    meal = mydata[12]
    adr = mydata[13]
    month = months.get(arrival_date_month)
    date = f"{arrival_date_year}-{month}-{arrival_date_day_of_month}"

    print(f"id = mydata[0]: {id}")

    data = {
    "id": id,
    "hotel": hotel,
    "is_canceled": is_canceled,
    "lead_time": lead_time,
    "arrival_date_year": arrival_date_year,
    "arrival_date_month": arrival_date_month,
    "arrival_date_day_of_month": arrival_date_day_of_month,
    "stays_in_weekend_nights": stays_in_weekend_nights,
    "stays_in_week_nights": stays_in_week_nights,
    "adults": adults,
    "children": children,
    "babies": babies,
    "meal": meal,
    "adr": adr,
    "date": date
    }

    return jsonify(data)
