# Business Registration API

A backend API system for managing business name registrations with role-based authentication and admin approval workflow.

---

## 🚀 Features

- Custom User Model (AbstractBaseUser)
- JWT Authentication
- Role-Based Access Control (User & Admin)
- Business Name Registration Submission
- Admin Approval System
- Status Tracking (Submitted, Approved)
- Document Upload System (for approved registrations)

---

## 🏗️ Tech Stack

- Python 3.13
- Django
- Django REST Framework
- Simple JWT
- SQLite (Development)

---

## 👤 User Roles

### Regular User
- Register account
- Login
- Submit business name registration
- View own registrations only

### Admin
- Login
- View all registrations
- Approve registrations
- Update registration status

---

## 🔐 Authentication

Uses JWT Authentication.

### Login Endpoint

POST `/api/auth/login/`

Request:
```json
{
  "email": "user@test.com",
  "password": "StrongPass123"
}

Response
{
  "refresh": "token",
  "access": "token"
}



📌 Main Endpoints
# Create Registration
POST /api/registrations/

##Get User Registrations
GET /api/registrations/

Admin Approve Registration
PATCH /api/registrations/<id>/approve/

Request:

{
  "approved_name": "Approved Business Name"
}
⚙️ Setup Instructions
Clone repository

Create virtual environment

python -m venv venv
Activate environment

Windows:

venv\Scripts\activate
Install dependencies

pip install -r requirements.txt
Run migrations

python manage.py migrate
Run server

python manage.py runserver
📊 System Workflow
User registers account

User logs in

User submits business name options

Admin reviews submission

Admin approves registration

Status updated to "approved"

📌 Author
Ayodele Ajisegiri