from re import M
import mysql.connector
import csv
import windowsgebruik

try:
    print("Status update: Wachten op verbinding maken met de database! \n")

    # verbinding maken met myphpadmin
    dbverbinding = mysql.connector.connect(
        host=windowsgebruik.krijgservernaam(),
        port=windowsgebruik.krijgpoort(),
        user=windowsgebruik.krijguser(),
        password=windowsgebruik.krijgwachtwoord(),
        database='hotel_booking'
    )

    print("Status update: Verbinding gemaakt met de database! \n")

    # csv inlezen
    data1 = None
    with open('./csv_bestanden/hotel_bookings.csv', 'r') as f:
        data1 = csv.reader(f)  # pakt alle rijen in een list

        mijncursor = dbverbinding.cursor()  # verbinding maken
        mijncursor.execute('DROP TABLE IF EXISTS hotel_booking;')
        mijncursor.execute('CREATE TABLE hotel_booking(id INT not null AUTO_INCREMENT, PRIMARY KEY (id), hotel VARCHAR(30), is_canceled INT, lead_time INT, arrival_date_year INT, arrival_date_month VARCHAR(30), arrival_date_day_of_month INT, stays_in_weekend_nights INT, stays_in_week_nights INT, adults INT, children INT, babies INT, meal VARCHAR(30), adr DECIMAL, date DATE);')

        print("Status update: Data in tabel nu toevoegen aan de database! \n")

        # pakt voor elke rij de juiste waarden van jaar, maand en maaltijd en kosten uit de dataset
        months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

        i = 0
        for row in data1:
            hotel = row[0]
            is_canceled = row[1]
            lead_time = row[2]
            arrival_date_year = row[3]
            arrival_date_month = row[4]
            arrival_date_day_of_month = row[6]
            stays_in_weekend_nights = row[7]
            stays_in_week_nights =  row[8]
            adults =  row[9]
            children = row[10]
            babies = row[11]
            meal = row[12]
            adr = row[27]
            month = months.get(arrival_date_month)
            date = f"{arrival_date_year}-{month}-{arrival_date_day_of_month}"

            if i != 0 and (float(adr) >= 80 and float(adr) <= 250):
                sql_insert_data = 'INSERT INTO hotel_booking (hotel, is_canceled, lead_time, arrival_date_year, arrival_date_month, arrival_date_day_of_month, stays_in_weekend_nights, stays_in_week_nights, adults, children, babies, meal, adr, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
                mijncursor.execute(sql_insert_data, (hotel, is_canceled, lead_time, arrival_date_year, arrival_date_month, arrival_date_day_of_month, stays_in_weekend_nights, stays_in_week_nights, adults, children, babies, meal, adr, date))  # execute(SQL statement, (hier de waarden voor de plekken %s en op volgorde)

                dbverbinding.commit() # data opsturen naar de database

            i += 1

            print(f"Status update: Data nummer {i} in tabel toegevoegd aan de database! \n")

    print("hotel_booking tabel is succesvol toegevoegd aan de database!")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if dbverbinding.is_connected():
        mijncursor.close()
        dbverbinding.close()
        print(f"MySQL connection is closed \n")