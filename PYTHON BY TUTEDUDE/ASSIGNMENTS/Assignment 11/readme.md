# 💻 Assignment 11: Flask Registration Form (Flask-WTF + SQLAlchemy)

## 📌 Project Overview
This project is a web-based registration system built using Flask.  
It allows users to enter their details, validates the input using Flask-WTF, stores data in a database using SQLAlchemy, and displays a success page.

---

## 🎯 Objective
- Learn Flask web framework  
- Implement Flask-WTF forms with validation  
- Use SQLAlchemy for database integration  
- Handle form submission and data storage  
- Build a complete form → validate → save → success flow  

---

## 🛠️ Technologies Used
- Python 3  
- Flask  
- Flask-WTF  
- SQLAlchemy  
- HTML  

---

## 📂 Project Structure

Assignment 11/  
│  
├── app.py  
│   → Main Flask application  
│   → Handles routing, form validation, and database operations  

├── forms.py  
│   → Contains Flask-WTF form class with validators  

├── models.py  
│   → Defines SQLAlchemy database model (User)  

├── README.md  
│   → Project documentation  

└── templates/  
    ├── register.html  
    │   → Registration form UI  
    │   → Displays validation errors  
    │  
    └── success.html  
        → Displays success message after registration  

---

## ⚙️ How It Works

### 🔹 Flask Backend
- Creates Flask application  
- Configures SECRET_KEY and database  
- Uses Flask-WTF for form handling  
- Validates user input (name, email, password)  
- Stores data in SQLite database  
- Redirects to success page after submission  

### 🔹 Form Validation
- Name → Required  
- Email → Must be valid format  
- Password → Required  
- Confirm Password → Must match  

### 🔹 Database (SQLAlchemy)
- Stores user details:
  - Name  
  - Email  
  - Password  

---

## 🚀 How to Run

### 1. Install required packages
```bash
pip install flask flask-wtf flask-sqlalchemy email_validator


2. Navigate to project folder
cd "Assignment 11"\

3. Run the application
python app.py

4. Open in browser
http://127.0.0.1:5000


🧪 Output

❗ Validation Errors
Empty fields → error message
Invalid email → error
Password mismatch → error

✅ Successful Submission
Registration Successful 🎉
Your data has been saved successfully.



### ⭐ Conclusion 
This project demonstrates how to build a simple web application using Flask and handle user input through forms.

## 👨‍🎓 Author - 
Kanishk Kumar Singh
