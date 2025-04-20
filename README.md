
# 🧾 Employee Management System

This **Employee Management System** is a Streamlit-based web application that manages employee records using a MySQL backend. It allows users to view and manage employee, department, project, attendance, and salary data through a secure login portal.

## 🚀 Features

- 👥 View and manage employee details
- 🏢 View department, project, and benefit information
- 📅 Track attendance and leave records
- 💰 Manage salaries and login credentials
- 🔐 Admin/Employee login system
- 📊 Streamlit-based interactive interface

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core language |
| Streamlit | Web interface |
| MySQL | Backend database |
| pandas | Data handling |
| mysql-connector-python | Database connectivity |

## 📂 Files Included

- `Newmain.py` – Main application file with all logic
- `Employee Management System Project.sql` – SQL file to set up the database schema

## ⚙️ How to Run

1. Install the required libraries:
   ```bash
   pip install streamlit pandas mysql-connector-python
   ```

2. Ensure MySQL server is running and the database is created using the provided SQL script.

3. Update the connection settings in `Newmain.py` (host, user, password, and database).

4. Launch the app:
   ```bash
   streamlit run Newmain.py
   ```

## 🔐 Default Credentials

Modify or create users in the `login` table of your MySQL database.

## 📌 Future Improvements

- Add role-based access for managers and HR
- Upload/download employee reports
- Add email notification integration

## 👩‍💻 Author

**Sri Harshita Prata**  
