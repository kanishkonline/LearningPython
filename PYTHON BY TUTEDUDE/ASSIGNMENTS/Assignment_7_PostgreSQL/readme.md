# Assignment 7: PostgreSQL with Python (psycopg2)

## 📌 Objective

The objective of this assignment is to demonstrate how to connect Python with PostgreSQL using the psycopg2 library and perform basic database operations (CRUD).

---

## 🛠️ Technologies Used

* Python 3.11
* PostgreSQL
* psycopg2 (Python library)

---

## 📂 Project Structure

Assignment_7/
│
├── code/
│   ├── 1_create_table.py
│   ├── 2_insert_data.py
│   ├── 3_fetch_data.py
│   ├── 4_update_data.py
│   ├── 5_delete_data.py
│
├── screenshots/
│   ├── 1_create.png
│   ├── 2_insert.png
│   ├── 3_fetch_before.png
│   ├── 4_update.png
│   ├── 5_fetch_after_update.png
│   ├── 6_delete.png
│   ├── 7_fetch_after_delete.png

---

## ⚙️ Steps Performed

### 1. Create Table

* A table named `employees` is created using SQL.
* Columns: id, name, age, department.

### 2. Insert Data

* Two records are inserted into the table.

### 3. Fetch Data

* All records are retrieved and displayed using SELECT query.

### 4. Update Data

* The age of an employee is updated.

### 5. Delete Data

* A record is deleted from the table.

---

## 🔄 Execution Order

The files are executed in the following order:

1. 1_create_table.py
2. 2_insert_data.py
3. 3_fetch_data.py
4. 4_update_data.py
5. 3_fetch_data.py (to verify update)
6. 5_delete_data.py
7. 3_fetch_data.py (to verify deletion)

---

## 📸 Output

Screenshots are provided in the `screenshots` folder showing:

* Code execution
* Output results
* System time for verification

---

## ✅ Conclusion

This assignment successfully demonstrates how to perform Create, Read, Update, and Delete (CRUD) operations in PostgreSQL using Python. It also shows how Python can be integrated with databases for real-world applications.

---

## 👨‍💻 Author

Name: Kanishk Singh
