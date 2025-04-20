import streamlit as st
import pandas as pd
import datetime
import mysql.connector
st.markdown("<center><h1>Employee Management System</h1><center>", unsafe_allow_html = True)
choice = st.sidebar.selectbox("My Menu",("Home", "Not an Employee", "Employee/Admin"))
st.write(choice)
if choice == "Home":
    st.markdown("<center><h1>Welcome</h1><center>", unsafe_allow_html = True)
    st.image("https://wortal.co/wp-content/uploads/2024/01/06-What-is-Employee-Management_-Understanding-an-Effective-Employee-Management-System.webp")
    st.write("This is a Web Application developed by Sri Harshita as part of Training Project.")
    
elif choice == "Not an Employee":
    choice1 = st.selectbox("Features", ("None", "View all employee details", "View all Department details", "View all benifits details", "View all projects Details"))
    if choice1 == "View all employee details":
        mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
        df = pd.read_sql("Select * from employee", mysd)
        st.dataframe(df)
    elif choice1 == "View all Department details":
        mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
        df = pd.read_sql("select * from department", mysd)
        st.dataframe(df)
    elif choice1 == "View all benifits details":
        mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
        df = pd.read_sql("select * from Benifits", mysd)
        st.dataframe(df)
    elif choice1 == "View all projects Details":
        mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
        df = pd.read_sql("select * from project", mysd)
        st.dataframe(df)

elif choice == "Employee/Admin":
    if 'login' not in st.session_state:
        st.session_state['login'] = False
    login = False
    user_id = st.text_input("Enter User ID: ")
    user_pass = st.text_input("Enter the password: ")
    login_button = st.button("Login")
    if login_button:
        mysd = mysql.connector.connect(host = "localhost", user = "root", password = "12345678", database = "Employees")
        c = mysd.cursor()
        c.execute("select * from login")
        for r in c:
            if r[0] == user_id and r[1] == user_pass:
                st.session_state['login'] = True
                break
        if (not st.session_state['login']):
            st.write("Invalid user ID or password")
    if(st.session_state['login']):
        st.write("Login successful")
        choice2 = st.selectbox("Features", ("None", "View employee details", "View department details", "View attendence details", "View break details", "View Benefits details", "View login details", "View project details", "View Salary details", "Add employee details", "Add department details", "Add attendence details", "Add break details", "Add Benefits details", "Add login details", "Add Project details", "Add Salaries details", "Delete employee details", "Delete login details"))
        if choice2 == "View employee details":
            mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
            df = pd.read_sql("Select * from employee", mysd)
            st.dataframe(df)
        elif choice2 == "View department details":
            mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
            df = pd.read_sql("select * from department", mysd)
            st.dataframe(df)
        elif choice2 == "View attendence details":
            mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
            df = pd.read_sql("select * from attendence", mysd)
            st.dataframe(df)
        elif choice2 == "View break details":
            mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
            df = pd.read_sql("select * from break", mysd)
            st.dataframe(df)
        elif choice2 == "View Benefits details":
            mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
            df = pd.read_sql("select * from Benifits", mysd)
            st.dataframe(df)
        elif choice2 == "View login details":
            mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
            df = pd.read_sql("select * from login", mysd)
            st.dataframe(df)
        elif choice2 == "View project details":
            mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
            df = pd.read_sql("select * from project", mysd)
            st.dataframe(df)
        elif choice2 == "View Salary details":
            mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
            df = pd.read_sql("select * from Salaries", mysd)
            st.dataframe(df)

            
        elif choice2 == "Add employee details":
            mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
            EmployeeID = st.text_input("EmployeeID")
            First_Name = st.text_input("First_Name")
            Last_Name = st.text_input("Last_Name")
            Middle_Name = st.text_input("Middle_Name")
            DOB = st.text_input("Date of birth")
            Gender = st.text_input("Gender")
            Marital_Status = st.text_input("Marital status")
            Address = st.text_input("Address")
            Phone_Number = st.text_input("Phone Number")
            Email = st.text_input("Email")
            Job_Title = st.text_input("Job_Title")
            Salary = st.text_input("Salary")
            DepartmentID = st.text_input("DepartmentID")
            ManagerID = st.text_input("ManagerID")
            button2 = st.button("Add")
            if button2:
                added_Time = str(datetime.datetime.now())
                mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
                c = mysd.cursor()
                c.execute("insert into employee values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (EmployeeID, First_Name, Last_Name, Middle_Name, DOB, Gender, Marital_Status, Address, Phone_Number, Email, Job_Title, Salary, DepartmentID, ManagerID))
                mysd.commit()
                st.header("Employee details added successfully")
        elif choice2 == "Add department details":
            mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
            DepartmentID = st.text_input("DepartmentID")
            Department_Name = st.text_input("Department Name")
            ManagerID = st.text_input("ManagerID")
            button2 = st.button("Add")
            if button2:
                added_Time = str(datetime.datetime.now())
                mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
                c = mysd.cursor()
                c.execute("insert into department values(%s, %s, %s)", (DepartmentID, Department_Name, ManagerID))
                mysd.commit()
                st.header("Department details added successfully")
        elif choice2 == "Add attendence details":
            mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
            AttendenceID = st.text_input("AttendenceID")
            EmployeeID = st.text_input("EmployeeID")
            Date = st.text_input("Date")
            attendence = st.text_input("attendence (present/absent/On duty/late)")
            button2 = st.button("Add")
            if button2:
                added_Time = str(datetime.datetime.now())
                mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
                c = mysd.cursor()
                c.execute("insert into Attendence values(%s, %s, %s, %s)", (AttendenceID, EmployeeID, Date, attendence))
                mysd.commit()
                st.header("Attendence details added successfully")
        elif choice2 == "Add break details":
            mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
            LeaveID = st.text_input("Leave ID")
            EmployeeID = st.text_input("EmployeeID")
            Leave_Type = st.text_input("Leave Type")
            From_Date = st.text_input("From Date")
            To_Date = st.text_input("To Date")
            leave_Status = st.text_input("leave Status (Approved, Not Approved, pending)")
            Reason = st.text_input("Reason")
            button2 = st.button("Add")
            if button2:
                added_Time = str(datetime.datetime.now())
                mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
                c = mysd.cursor()
                c.execute("insert into Break values(%s, %s, %s, %s, %s, %s, %s)", (LeaveID, EmployeeID, Leave_Type, From_Date, To_Date, leave_Status, Reason))
                mysd.commit()
                st.header("Leave/Break details added successfully")
        elif choice2 == "Add Benefits details":
            mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
            BenefitID = st.text_input("BenefitID")
            Benefit_Type = st.text_input("Benefit Type")
            Benefit_Description = st.text_input("Benefit Description")
            Eligibility_Criteria = st.text_input("Eligibility Criteria")
            button2 = st.button("Add")
            if button2:
                added_Time = str(datetime.datetime.now())
                mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
                c = mysd.cursor()
                c.execute("insert into Benifits values(%s, %s, %s, %s)", (BenefitID, Benefit_Type, Benefit_Description, Eligibility_Criteria))
                mysd.commit()
                st.header("Benifits details added successfully")
        elif choice2 == "Add login details":
            mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
            Username = st.text_input("Username")
            passkey = st.text_input("passkey")
            button2 = st.button("Add")
            if button2:
                added_Time = str(datetime.datetime.now())
                mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
                c = mysd.cursor()
                c.execute("insert into login values(%s, %s)", (Username, passkey))
                mysd.commit()
                st.header("Login details added successfully")
        elif choice2 == "Add Project details":
            mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
            ProjectID = st.text_input("ProjectID")
            Project_Name = st.text_input("Project Name")
            Start_Date = st.text_input("Start Date")
            End_date = st.text_input("End date")
            Analysis = st.text_input("Analysis")
            button2 = st.button("Add")
            if button2:
                added_Time = str(datetime.datetime.now())
                mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
                c = mysd.cursor()
                c.execute("insert into project values(%s, %s, %s, %s, %s)", (ProjectID, Project_Name, Start_Date, End_date, Analysis))
                mysd.commit()
                st.header("Project details added successfully")
        elif choice2 == "Add Salaries details":
            mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
            SalaryID = st.text_input("SalaryID")
            EmployeeID = st.text_input("EmployeeID")
            Salary = st.text_input("Salary")
            Effective_Date = st.text_input("Effective Date")
            button2 = st.button("Add")
            if button2:
                added_Time = str(datetime.datetime.now())
                mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
                c = mysd.cursor()
                c.execute("insert into Salaries values(%s, %s, %s, %s)", (SalaryID, EmployeeID, Salary, Effective_Date))
                mysd.commit()
                st.header("Salaries details added successfully")

        elif choice2 == "Delete employee details":
            EmployeeID = st.text_input("EmployeeID")
            Delete_button = st.button("Delete")
            if Delete_button:
                mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
                c = mysd.cursor()
                c.execute("delete from employee where EmployeeID = %s", (EmployeeID,))
                mysd.commit()
                st.header("Employee details deleted successfully")
        elif choice2 == "Delete login details":
            Username = st.text_input("Username")
            Delete_button = st.button("Delete")
            if Delete_button:
                mysd=mysql.connector.connect(host = "localhost", user = "root", password= "12345678", database ="Employees")
                c = mysd.cursor()
                c.execute("delete from login where Username = %s", (Username,))
                mysd.commit()
                st.header("Login details deleted successfully")










        
