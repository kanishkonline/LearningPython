# Assignment 7 - Task 5: Delete Data
import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="2486",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("DELETE FROM employees WHERE name = 'Rahul';")

print("Data Deleted Successfully")

conn.commit()
conn.close()