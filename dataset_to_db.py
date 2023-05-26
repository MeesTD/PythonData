import mysql.connector
import csv

# verbinding maken met myphpadmin
dbverbinding = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='',
    database='hotel_booking'
)

# als connectie gemaakt is, het geeft niks terug, dan is het goed gelukt. een check.
print("test")

# tutorial van python 4 data verzamelen
"""mijncursor = dbverbinding.cursor()
mijncursor.execute("SELECT * FROM fiets")
allefietsen = mijncursor.fetchall()
print(allefietsen)"""

# csv inlezen
data1 = None
with open('./csv_bestanden/hotel_bookings.csv', 'r') as f:
    data1 = csv.reader(f) # pakt alle rijen in een list
    

    mijncursor = dbverbinding.cursor() # verbinding maken
    mijncursor.execute('DROP TABLE IF EXISTS hotel_booking;')
    mijncursor.execute('CREATE TABLE hotel_booking(id INT not null AUTO_INCREMENT, PRIMARY KEY (id), arrival_date_year INT, arrival_date_month VARCHAR(30), arrival_date_day_of_month INT, meal VARCHAR(30), adr DECIMAL);')
    
    # maakt nieuwe tabel aan met hotel_booking, id is primary key
    #mijncursor.execute('CREATE TABLE hotel_booking(id INT not null AUTO_INCREMENT, PRIMARY KEY (id));')
    # maakt tabel attribuut aan voor jaar, maand en land die overeenkomen met de dataset header
    #mijncursor.execute('ALTER TABLE hotel_booking ADD (arrival_date_year INT, arrival_date_month VARCHAR(30), arrival_date_day_of_month INT, meal VARCHAR(30), adr DECIMAL)')

    # pakt voor elke rij de juiste waarden van jaar, maand en maaltijd en kosten uit de dataset
    for row in data1:
        arrival_date_year = row[3]
        arrival_date_month = row[4]
        arrival_date_day_of_month = row[6]
        meal = row[12]
        adr = row[27]
        # voeg wwaarden toe aan de attributen in de tabel voor jaar, maand en land met de waarden die gelijk zijn aan het index nummer op die volgorde op de plek van %s
        sql_insert_data = 'INSERT INTO hotel_booking (arrival_date_year, arrival_date_month, arrival_date_day_of_month, meal, adr) VALUES (%s, %s, %s, %s, %s);'
        mijncursor.execute(sql_insert_data, (arrival_date_year, arrival_date_month, arrival_date_day_of_month, meal, adr)) # execute(SQL statement, (hier de waarden voor de plekken %s en op volgorde)))
    
    # rijen toegevoegd bijhouden
    aantal_rijen_ingevoegd = mijncursor.rowcount
    print(aantal_rijen_ingevoegd)

# data opsturen naar de database
dbverbinding.commit()

# dataverbinding afsluiten
dbverbinding.close()

"""for f in allefietsen:
    print(f[1])"""
