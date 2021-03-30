# Import Lib
import mysql.connector

# Make Connection
cnx = mysql.connector.connect(
    host = "localhost",
    user = "neotrinost",
    password = "neotrinost",
    database = "neotrinost"
)

# Make Cursor
cursor = cnx.cursor()

# Select Data Query
cursor.execute("SELECT * FROM admin")

# Loop in Cursor
for (usrname, passwd) in cursor:
    # Get data
    username = usrname
    password = passwd