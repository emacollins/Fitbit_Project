import Fitbit as fb
import sqlite3

df_sleep = fb.sleep_data()
df_zone_minutes = fb.zone_minutes()

con = sqlite3.connect("fitbit_data.db")

# Write the new DataFrame to a new SQLite table
df_zone_minutes.to_sql("Zone_Minutes", con, if_exists="replace")
df_sleep.to_sql("Sleep", con, if_exists="replace")

con.close()

#Git test change
#Git test change 2 

