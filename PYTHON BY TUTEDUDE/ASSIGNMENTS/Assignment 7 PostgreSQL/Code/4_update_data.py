# Assignment 7 - Task 4: Update Data
import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="2486",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("UPDATE employees SET age = 25 WHERE name = 'Kanishk';")

print("Data Updated Successfully")

conn.commit()
conn.close()