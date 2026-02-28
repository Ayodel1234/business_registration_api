🚀 Business Registration API

A production-style backend API for managing business name registrations with role-based authentication, approval workflow, document management, and query handling.

This project simulates a real-world business registration workflow similar to Corporate Affairs Commission (CAC) processes.


🏗️ Tech Stack

Python 3.13
Django 6
Django REST Framework
Simple JWT (Authentication)
SQLite (Development)
Custom User Model (AbstractBaseUser)


🔥 Core Features
✅ Authentication & Security
Custom User Model (email-based login)
JWT Authentication (access & refresh tokens)
Role-based access control (Admin & Regular User)
Global authentication enforcement

✅ Registration Workflow
Business Name & LTD registration submission
Multiple name options
Status tracking system:
submitted
queried
responded
name_approved
rejected
completed

✅ Admin Workflow
View all registrations
Approve registration
Reject registration
Raise query
View dashboard analytics
Filter registrations by status

✅ Query & Response System
Admin can raise query on a registration
User can respond to query
Status automatically updates

✅ Document Management System
Upload official documents (Admin only)
Upload supporting documents (User only)
Document access restricted by role
File storage using Django media system

✅ API Enhancements
Pagination (PageNumberPagination)
Status filtering via query parameters
Proper HTTP status codes (200, 201, 400, 403)


👤 User Roles

🔹 Regular User

Register account
Login
Submit registration
View only own registrations
Respond to admin queries
View own documents


🔹 Admin

Login
View all registrations
Approve registration
Reject registration
Raise query
Upload official documents
View dashboard analytics


🔐 Authentication
JWT Authentication is used.

Login
POST /api/auth/login/

Request:
{
  "email": "user@test.com",
  "password": "StrongPass123"
}

Response:

{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}

Use access token in headers:
Authorization: Bearer <access_token>


📌 API Endpoints


🔹 Authentication
Method	Endpoint
POST	/api/auth/login/
POST	/api/auth/refresh/


🔹 Registrations
Method	Endpoint	Description
POST	/api/registrations/	Create registration
GET	/api/registrations/	List registrations (role-based)
GET	/api/registrations/<id>/	Retrieve single registration
PATCH	/api/registrations/<id>/approve/	Admin approve
PATCH	/api/registrations/<id>/reject/	Admin reject
PATCH	/api/registrations/<id>/query/	Admin raise query
PATCH	/api/registrations/<id>/respond/	User respond


🔹 Filtering

Filter by status:
GET /api/registrations/?status=submitted
GET /api/registrations/?status=name_approved
GET /api/registrations/?status=rejected


🔹 Pagination

Default page size: 5
Example:
GET /api/registrations/?page=2


🔹 Documents
Method	Endpoint	Description
GET	/api/documents/	List documents (role-based)
POST	/api/documents/upload/	Upload document


Document rules:
Admin uploads official documents (certificate, memart, etc.)
Users upload supporting documents only
Upload restricted unless registration is approved


🔹 Admin Dashboard
GET /api/admin/dashboard/
Returns:
{
  "total_registrations": 15,
  "submitted": 4,
  "queried": 2,
  "name_approved": 5,
  "rejected": 4
}


📊 System Workflow

User registers account
User logs in
User submits registration
Admin reviews submission

Admin can:
Approve
Reject
Raise query
User responds to query (if any)
Admin uploads official documents after approval
Registration marked completed



🗄️ Database Design

Main Entities:
User (Custom)
Registration
Document

Relationships:
One User → Many Registrations
One Registration → Many Documents
One Document → Uploaded by User/



⚙️ Setup Instructions
1️⃣ Clone Repository
git clone <your_repo_url>
cd business_registration_api
2️⃣ Create Virtual Environment
python -m venv venv
Activate (Windows):
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate
5️⃣ Create Superuser
python manage.py createsuperuser
6️⃣ Run Server
python manage.py runserver


🧪 Testing

You can test using:
Postman
Swagger (if enabled)
Django Admin



📌 Future Improvements

Payment integration
Email notifications
Cloud storage (AWS S3)
Agent subscription system
Wallet system
CAC API integration



📎 Author

Ayodele Ajisegiri
Backend Engineering Capstone Project
ALX Africa



🏁 Capstone Notes

This project demonstrates:
Clean architecture
Role-based access control
Proper RESTful endpoint structure
Secure authentication
Business workflow modeling
Query handling logic
Document management system
Pagination & filtering
Admin analytics