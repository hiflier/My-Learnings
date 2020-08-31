' #!/usr/bin/python3 '
import mysql.connector

#establishing the connection
conn = mysql.connector.connect(
   user='root', password='root', host='35.224.84.147', database='authors')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL query to INSERT a record into the database.
s_id = input('Author ID:')
s_name = input('Author name:')
insert_stmt = (
   "INSERT INTO author(authorID, authorname)"
   "VALUES (%s, %s)"
)
data = (s_id, s_name)

try:
   # Executing the SQL command
   cursor.execute(insert_stmt, data)
   
   # Commit your changes in the database
   conn.commit()

except:
   # Rolling back in case of error
   conn.rollback()

print("Data inserted")

# Closing the connection
conn.close()
if (conn):
	conn.close()
	print("Connection is closed.")