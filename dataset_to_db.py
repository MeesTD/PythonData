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
with open('./csv_bestanden/hotel_booking.csv', 'r') as f:
    data1 = csv.reader(f) # pakt alle rijen in een list
    
    mijncursor = dbverbinding.cursor() # verbinding maken
    # maakt nieuwe tabel aan met hotel_booking, id is primary key
    mijncursor.execute('CREATE TABLE hotel_booking(id INT not null AUTO_INCREMENT, PRIMARY KEY (id));')
    # maakt tabel attribuut aan voor jaar, maand en land die overeenkomen met de dataset header
    mijncursor.execute('ALTER TABLE hotel_booking ADD (arrival_date_year INT, arrival_date_month VARCHAR(30), country VARCHAR(50))')

    # pakt voor elke rij de juiste waarden van jaar, maand en land uit de dataset
    for row in data1:
        arrival_date_year = row[3]
        arrival_date_month = row[4]
        country = row[13]
        # voeg wwaarden toe aan de attributen in de tabel voor jaar, maand en land met de waarden die gelijk zijn aan het index nummer op die volgorde op de plek van %s
        sql_insert_data = 'INSERT INTO hotel_booking (arrival_date_year, arrival_date_month, country) VALUES (%s, %s, %s);'
        mijncursor.execute(sql_insert_data, (arrival_date_year, arrival_date_month, country)) # execute(SQL statement, (hier de waarden voor de plekken %s en op volgorde)))
    
    # rijen toegevoegd bijhouden
    aantal_rijen_ingevoegd = mijncursor.rowcount
    print(aantal_rijen_ingevoegd)

# data opsturen naar de database
dbverbinding.commit()

# dataverbinding afsluiten
dbverbinding.close()

"""for f in allefietsen:
    print(f[1])"""