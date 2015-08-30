from dbconfig import *
import mysql.connector
from datetime import datetime
from sense_hat import SenseHat

# Create SenseHat object

sense = SenseHat()

date_v = datetime.now()
humi_v = sense.get_humidity()
tmph_v = sense.get_temperature()
tmpp_v = sense.get_temperature_from_pressure()
pres_v = sense.get_pressure()

# Connect to MySQL

sql = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PWD, host=MYSQL_HOST, database=DATABASE_NAME)
cursor = sql.cursor()

updatetime = datetime.now()

data = ( TABLE_NAME, READ_DATE, READ_HUMI, READ_TMPH, READ_TMPP, READ_PRES, date_v, humi_v, tmph_v, tmpp_v, pres_v )

update_query = "INSERT INTO %s (%s, %s, %s, %s, %s) VALUES ('%s','%s','%s','%s','%s')" % data

cursor.execute(update_query)

sql.commit()
sql.close()
