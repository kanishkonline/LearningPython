# Assignment 7 - Task 1: Create Table
import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="2486",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id SERIAL PRIMARY KEY,
    name TEXT,
    age INT,
    department TEXT
);
""")

print("Table Created Successfully")

conn.commit()
conn.close()
