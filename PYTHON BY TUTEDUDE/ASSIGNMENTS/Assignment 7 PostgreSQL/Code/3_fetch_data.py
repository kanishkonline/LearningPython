# Assignment 7 - Task 3: Fetch Data
import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="2486",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM employees;")
rows = cursor.fetchall()

print("Employee Records:")
for row in rows:
    print(row)

conn.close()