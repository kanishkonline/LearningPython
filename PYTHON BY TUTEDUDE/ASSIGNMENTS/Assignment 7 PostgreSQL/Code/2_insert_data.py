# Assignment 7 - Task 2: Insert Data

import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="2486",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("INSERT INTO employees (name, age, department) VALUES ('Kanishk', 20, 'IT');")
cursor.execute("INSERT INTO employees (name, age, department) VALUES ('Rahul', 22, 'HR');")

print("Data Inserted Successfully")

conn.commit()
conn.close()