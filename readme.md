# 🏥 Doctor Patient Appointment Management System API
![project overview](image/pro.png)



![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql)
![JWT](https://img.shields.io/badge/JWT-Authentication-purple?style=for-the-badge)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge)


## 📌 Overview

**Doctor Patient Appointment Management System** is a secure RESTful Backend API developed using **FastAPI**.

The system allows patients to book appointments with doctors, doctors to manage appointment requests, and admins to manage the entire platform.

This project follows real-world backend architecture with:

✨ JWT Authentication  
✨ Role Based Authorization (RBAC)  
✨ Secure Password Hashing  
✨ Database Relationships  
✨ Ownership Based Access Control  
✨ Modular API Structure  


---

# 🚀 Features


## 🔐 Authentication & Security

✔ User Registration  
✔ User Login  
✔ JWT Access Token Authentication  
✔ Password Hashing using bcrypt  
✔ OAuth2 Password Bearer Authentication  
✔ Protected API Routes  


---

# 👥 User Roles


## 🛡 Admin

Admin has complete system control.

### Features:

✔ View all users  
✔ View all doctors  
✔ View all patients  
✔ View all appointments  
✔ Delete users  


---

## 👨‍⚕️ Doctor

Doctor can manage profile and appointments.

### Features:

✔ Create Doctor Profile  
✔ Update Doctor Profile  
✔ View Assigned Appointments  
✔ Accept Appointments  
✔ Reject Appointments  
✔ Mark Appointment as Completed  


---

## 🧑 Patient

Patient can search doctors and book appointments.

### Features:

✔ View Available Doctors  
✔ Search Doctor by Specialization  
✔ Book Appointment  
✔ View Own Appointments  
✔ Cancel Appointment  


---


# 🏗 Tech Stack


| Technology | Purpose |
|----------|---------|
| 🐍 Python | Programming Language |
| ⚡ FastAPI | Backend Framework |
| 🗄 MySQL | Database |
| 🔗 SQLAlchemy | ORM |
| 📦 Pydantic | Data Validation |
| 🔑 JWT | Authentication |
| 🔒 Passlib bcrypt | Password Hashing |
| 📘 Swagger UI | API Documentation |


---


# 🗄 Database Design


## Users Table


| Column | Description |
|-----|-------------|
| id | Primary Key |
| username | User Login Name |
| password | Hashed Password |
| role | admin / doctor / patient |



---

## Doctor Profile Table


| Column | Description |
|-----|-------------|
| id | Primary Key |
| user_id | ForeignKey(users.id) |
| specialization | Doctor Field |
| experience | Experience Years |
| availability | Available Timing |



---

## Appointment Table


| Column | Description |
|-----|-------------|
| id | Primary Key |
| patient_id | ForeignKey(users.id) |
| doctor_id | ForeignKey(doctor_profiles.id) |
| date | Appointment Date |
| time | Appointment Time |
| status | Appointment Status |


Status values:


pending
accepted
rejected
completed



---


# 🔗 Database Relationship


             USERS

      id
      username
      role

         |
         |
 -----------------
 |               |

DOCTOR PROFILE APPOINTMENT

id id

user_id patient_id

specialization doctor_id

experience status

availability



---


# 🔐 Authentication Flow



User Login

 ↓

Verify Password

 ↓

Generate JWT Token

 ↓

Send Token in Header

 ↓

OAuth2PasswordBearer

 ↓

get_current_user()

 ↓

Access Protected Routes



---


# 🏥 Appointment Flow



PATIENT

Search Doctor

  ↓

Book Appointment

  ↓

Status = Pending

==============================

DOCTOR

View Appointment

  ↓

Accept / Reject

  ↓

Status Updated

==============================

Treatment Finished

  ↓

Mark Completed



---


# 📂 Project Structure



doctor-appointment-system/

│── main.py

│── database.py

│── security.py

│

├── models/

│ └── alchemy_model.py

│

├── schemas/

│ └── schemas.py

│

├── routers/

│ ├── auth.py

│ ├── doctor.py

│ ├── patient.py

│ ├── appointment.py

│ └── admin.py

│

├── requirements.txt

├── .env.example

├── .gitignore

└── README.md



---


# 📡 API Endpoints


## 🔐 Authentication


| Method | Endpoint | Description |
|-|-|-|
| POST | `/auth/register` | Register User |
| POST | `/auth/login` | Login User |



---


# 👨‍⚕️ Doctor APIs


| Method | Endpoint | Description |
|-|-|-|
| POST | `/doctor/profile` | Create Profile |
| PUT | `/doctor/profile` | Update Profile |
| GET | `/doctor/appointments` | View Appointments |



---


# 🧑 Patient APIs


| Method | Endpoint | Description |
|-|-|-|
| GET | `/patient/doctors` | View Doctors |
| GET | `/patient/doctors/search` | Search Doctor |
| POST | `/patient/appointments` | Book Appointment |
| GET | `/patient/appointments` | My Appointments |
| DELETE | `/patient/appointments/{id}` | Cancel Appointment |



---


# 📅 Appointment APIs


| Method | Endpoint | Description |
|-|-|-|
| PUT | `/appointment/{id}/accept` | Accept Appointment |
| PUT | `/appointment/{id}/reject` | Reject Appointment |
| PUT | `/appointment/{id}/complete` | Complete Appointment |



---


# 🛡 Admin APIs


| Method | Endpoint | Description |
|-|-|-|
| GET | `/admin/users` | View Users |
| GET | `/admin/doctors` | View Doctors |
| GET | `/admin/patients` | View Patients |
| GET | `/admin/appointments` | View Appointments |
| DELETE | `/admin/users/{id}` | Delete User |



---


# ⚙ Installation & Setup


### 1️⃣ Clone Repository


```bash
git clone https://github.com/username/doctor-appointment-system.git
2️⃣ Create Virtual Environment
python -m venv venv

Activate:

Windows

venv\Scripts\activate

Linux/Mac

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Configure Environment

Create .env file:

DATABASE_URL=mysql+pymysql://username:password@localhost/database

SECRET_KEY=your_secret_key

ALGORITHM=HS256
5️⃣ Run Application
uvicorn main:app --reload
📘 API Documentation

Swagger UI:

http://localhost:8000/docs

ReDoc:

http://localhost:8000/redoc
⭐ Backend Concepts Implemented

✔ REST API Architecture
✔ Modular Router Structure
✔ Dependency Injection
✔ ORM Relationships
✔ JWT Authentication
✔ Role Based Access Control
✔ Password Encryption
✔ Database Relationships
✔ Ownership Authorization
✔ Error Handling
✔ Swagger Documentation

🎯 Future Improvements

🔹 Email Notification System
🔹 Appointment Reminder
🔹 Payment Integration
🔹 Docker Deployment

👨‍💻 Author

shravan

Backend Developer | Python | FastAPI

⭐ If you like this project, give it a star!


This README will look professional on GitHub and clearly shows recruiters that the project is beyond basic CRUD.
