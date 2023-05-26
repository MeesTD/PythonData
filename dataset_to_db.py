from re import M
import mysql.connector
import csv

# verbinding maken met myphpadmin
dbverbinding = mysql.connector.connect(
    host='localhost',
    port='8889',
    user='root',
    password='root',
    database='hotel_booking'
)

# als connectie gemaakt is, het geeft niks terug, dan is het goed gelukt. een check.
print("test")

# csv inlezen
data1 = None
with open('./csv_bestanden/hotel_bookings.csv', 'r') as f:
    data1 = csv.reader(f) # pakt alle rijen in een list

    mijncursor = dbverbinding.cursor() # verbinding maken
    mijncursor.execute('DROP TABLE IF EXISTS hotel_booking;')
    mijncursor.execute('CREATE TABLE hotel_booking(id INT not null AUTO_INCREMENT, PRIMARY KEY (id), hotel VARCHAR(30), arrival_date_year INT, arrival_date_month VARCHAR(30), arrival_date_day_of_month INT, meal VARCHAR(30), adr DECIMAL, date DATE);')
    
    # pakt voor elke rij de juiste waarden van jaar, maand en maaltijd en kosten uit de dataset
    months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

    i = 0
    for row in data1:
        hotel = row[0]
        arrival_date_year = row[3]
        arrival_date_month = row[4]
        arrival_date_day_of_month = row[6]
        meal = row[12]
        adr = row[27]
        month = months.get(arrival_date_month)
        date = f"{arrival_date_year}-{month}-{arrival_date_day_of_month}"
        
        if i != 0:
            sql_insert_data = 'INSERT INTO hotel_booking (hotel, arrival_date_year, arrival_date_month, arrival_date_day_of_month, meal, adr, date) VALUES (%s, %s, %s, %s, %s, %s, %s);'
            mijncursor.execute(sql_insert_data, (hotel, arrival_date_year, arrival_date_month, arrival_date_day_of_month, meal, adr, date)) # execute(SQL statement, (hier de waarden voor de plekken %s en op volgorde)))
            # data opsturen naar de database
            dbverbinding.commit()
    
            # data opsturen naar de database
            dbverbinding.commit()

        i += 1

# dataverbinding afsluiten
dbverbinding.close()