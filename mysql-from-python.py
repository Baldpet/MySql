import os
import datetime
import pymysql

# Get username from Gitpod

username = os.getenv('Gitpod_User')

# Connect to the database
connection = pymysql.connect(
    host='localhost', user=username, password='', db='Chinook')

try:
    # Run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                         Friends(Name char(20), age int, DOB datetime);""")

finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
