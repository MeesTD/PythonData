import mysql
import windowsgebruik

def show():
    print ("Iets in dit programma")
    return ("In ieder geval een string")

def plot(da, db):
    dbverbinding = mysql.connector.connect(
        host=windowsgebruik.krijgservernaam(),
        port=windowsgebruik.krijgpoort(),
        user=windowsgebruik.krijguser(),
        password=windowsgebruik.krijgwachtwoord(),
        database='hotel_booking'
    )
    mijncursor = dbverbinding.cursor()
    sql_check_data = "SELECT distinct date, avg(lead_time) as lead FROM hotel_booking.hotel_booking WHERE date >= '"+da+"' AND date <= '"+db+"' GROUP BY date;"
    print(sql_check_data)
    mijncursor.execute(sql_check_data) # execute(SQL statement, (hier de waarden voor de plekken %s en op volgorde)
    mydata = mijncursor.fetchall()

    keys = [i[0] for i in mijncursor.description]

    data = [
        dict(zip(keys, row)) for row in mydata
    ]
    return data
