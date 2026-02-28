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


---

# 🔐 Environment Variables

For security, sensitive settings should be stored in a `.env` file in production.

Example `.env` file:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost


⚠️ Note: This project currently uses settings.py for development.
In production, environment variables should be used instead of hardcoded values.


📡 Example API Requests (cURL)
🔐 Login
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
-H "Content-Type: application/json" \
-d '{
  "email": "admin@test.com",
  "password": "AdminPass123"
}'


📝 Create Registration
curl -X POST http://127.0.0.1:8000/api/registrations/ \
-H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
-H "Content-Type: application/json" \
-d '{
  "service_type": "business_name",
  "name_option_1": "Alpha Tech Solutions",
  "name_option_2": "Alpha Innovations"
}'


✅ Approve Registration (Admin Only)
curl -X PATCH http://127.0.0.1:8000/api/registrations/4/approve/ \
-H "Authorization: Bearer ADMIN_ACCESS_TOKEN" \
-H "Content-Type: application/json" \
-d '{
  "approved_name": "Alpha Tech Solutions"
}'


🔄 System Workflow Diagram
User Registers Account
        │
        ▼
User Logs In (JWT Issued)
        │
        ▼
User Submits Business Name Options
        │
        ▼
Admin Reviews Submission
        │
        ├── Reject → Status: rejected
        │
        └── Approve → Status: name_approved
                          │
                          ▼
                Admin Uploads Official Certificate
                          │
                          ▼
                    Status: completed
🧪 Sample Test Credentials

You can create these manually via admin panel or registration endpoint.


👤 Regular User
Email: user@test.com
Password: UserPass123
Role: user

👑 Admin User
Email: admin@test.com
Password: AdminPass123
Role: admin

⚠️ These are example credentials for local development only.


📁 Project Structure
accounts/        → Custom user model & authentication
registrations/   → Business registration workflow
documents/       → Document upload & restrictions
config/          → Project settings and root configuration


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


