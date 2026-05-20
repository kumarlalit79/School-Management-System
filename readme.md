# School Management API
> A FastAPI backend for managing school departments, students, teachers, and JWT-based access control.

## Repository Description
FastAPI school management backend with students, teachers, departments, PostgreSQL, JWT auth, and role-based access.

## Demo
Live link, demo video, or screenshots can be added here later.

When the server is running locally:

- API root: `http://127.0.0.1:8000/`
- Swagger docs: `http://127.0.0.1:8000/docs`
- ReDoc docs: `http://127.0.0.1:8000/redoc`

## Description
This project is a school management REST API built with FastAPI and Python. It manages students, teachers, and departments using SQLAlchemy models, Pydantic validation, PostgreSQL storage, and JWT authentication.

The codebase is also structured as a practical learning project: it shows how a backend grows from simple routes into separated layers for models, schemas, CRUD logic, database sessions, authentication, and role-based authorization.

## Tech Stack
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white)

## Features
- Student CRUD APIs for creating, reading, updating, and deleting student records.
- Teacher CRUD APIs for creating, reading, updating, and deleting teacher records.
- Department CRUD APIs for managing department names and building locations.
- SQLAlchemy relationships between departments, students, and teachers.
- Pydantic schemas for request validation and response formatting.
- Password hashing with `bcrypt` before storing user passwords.
- JWT login endpoint for student authentication.
- Protected routes with current-user extraction and role-based access checks.

## How It Works
1. The user starts the FastAPI server with Uvicorn.
2. FastAPI creates database tables from the SQLAlchemy models.
3. The user creates departments, students, and teachers through REST endpoints.
4. Student and teacher passwords are hashed before records are saved.
5. A student logs in with email and password through `/auth/login`.
6. The API returns a bearer token containing the user's email, role, and id.
7. Protected routes read the token, verify it, and return the logged-in user payload.
8. Role-protected routes allow access only when the token role matches the allowed roles.

Authentication flow:

```text
User Login Request
    -> /auth/login
    -> Find student by email
    -> Verify bcrypt password
    -> Create JWT access token
    -> Return bearer token
    -> Use token on protected routes
```

Data flow:

```text
Client Request
    -> FastAPI Route
    -> Pydantic Schema Validation
    -> CRUD Function
    -> SQLAlchemy Session
    -> PostgreSQL Database
    -> Response Model
    -> JSON Response
```

## Learning Curve
This project shows a clear backend learning path:

1. Start with a basic FastAPI app and root health route.
2. Add SQLAlchemy database connection and session dependency.
3. Create database models for real entities.
4. Add Pydantic schemas to separate input and output data.
5. Move database operations into CRUD modules.
6. Organize endpoints into route files by feature.
7. Add password hashing for safer authentication.
8. Add JWT login, protected routes, and role-based authorization.

## Project Structure
```text
.
├── app/
│   ├── core/
│   │   ├── config.py          # Loads environment variables
│   │   └── security.py        # Password hashing, JWT creation, token verification, role checks
│   ├── crud/
│   │   ├── department.py      # Department database operations
│   │   ├── student.py         # Student database operations
│   │   └── teacher.py         # Teacher database operations
│   ├── db/
│   │   ├── database.py        # SQLAlchemy engine, session, and Base setup
│   │   └── dependencies.py    # FastAPI database session dependency
│   ├── models/
│   │   ├── __init__.py        # Imports all SQLAlchemy models
│   │   ├── department.py      # Department model and relationships
│   │   ├── student.py         # Student model
│   │   └── teacher.py         # Teacher model
│   ├── routes/
│   │   ├── auth.py            # Login route
│   │   ├── department.py      # Department endpoints and role-protected examples
│   │   ├── student.py         # Student endpoints and protected profile route
│   │   └── teacher.py         # Teacher endpoints
│   ├── schemas/
│   │   ├── auth.py            # Login and token response schemas
│   │   ├── department.py      # Department request and response schemas
│   │   ├── student.py         # Student request and response schemas
│   │   └── teacher.py         # Teacher request and response schemas
│   └── main.py                # FastAPI app setup and router registration
├── .env                       # Local environment variables
├── .gitignore                 # Ignored files and folders
├── readme.md                  # Project documentation
└── requirements.txt           # Python dependencies
```

## Getting Started

### Prerequisites
- Python 3.10 or higher
- PostgreSQL installed and running
- Git
- A Python virtual environment tool such as `venv`

### Installation
Clone the repository:

```bash
git clone https://github.com/kumarlalit79/3_school_management_project.git
cd 3_school_management_project
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS or Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a PostgreSQL database, then add your connection string and security settings in `.env`.

Run the API:

```bash
uvicorn app.main:app --reload
```

Open the API documentation:

```text
http://127.0.0.1:8000/docs
```

### Environment Variables
| Variable | Description | Example |
| --- | --- | --- |
| `DATABASE_URL` | PostgreSQL connection string used by SQLAlchemy | `postgresql://postgres:password@localhost:5432/fastapi_learning` |
| `SECRET_KEY` | Secret key used to sign JWT access tokens | `change-this-secret-key` |
| `ALGORITHM` | JWT signing algorithm | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiry time in minutes | `30` |

## API Endpoints

### Base
| Method | Route | Description |
| --- | --- | --- |
| `GET` | `/` | Check whether the API is running. |

### Authentication
| Method | Route | Description |
| --- | --- | --- |
| `POST` | `/auth/login` | Log in a student and return a JWT bearer token. |

### Students
| Method | Route | Description |
| --- | --- | --- |
| `POST` | `/students/` | Create a student. |
| `GET` | `/students/` | Get all students. |
| `GET` | `/students/me` | Get the current authenticated user payload. |
| `GET` | `/students/{student_id}` | Get one student by id. |
| `PUT` | `/students/{student_id}` | Update a student by id. |
| `DELETE` | `/students/{student_id}` | Delete a student by id. |

### Teachers
| Method | Route | Description |
| --- | --- | --- |
| `POST` | `/teacher/` | Create a teacher. |
| `GET` | `/teacher/` | Get all teachers. |
| `GET` | `/teacher/{teacher_id}` | Get one teacher by id. |
| `PUT` | `/teacher/{teacher_id}` | Update a teacher by id. |
| `DELETE` | `/teacher/{teacher_id}` | Delete a teacher by id. |

### Departments
| Method | Route | Description |
| --- | --- | --- |
| `POST` | `/departments/` | Create a department. |
| `GET` | `/departments/` | Get all departments. |
| `GET` | `/departments/admin-only` | Example route for users with the `admin` role. |
| `GET` | `/departments/staff-only` | Example route for users with the `admin` or `teacher` role. |
| `GET` | `/departments/{department_id}` | Get one department by id. |
| `PUT` | `/departments/{department_id}` | Update a department by id. |
| `DELETE` | `/departments/{department_id}` | Delete a department by id. |

## Data Models

### Department
| Field | Type | Notes |
| --- | --- | --- |
| `id` | Integer | Primary key |
| `name` | String | Required and unique |
| `building` | String | Required |

### Student
| Field | Type | Notes |
| --- | --- | --- |
| `id` | Integer | Primary key |
| `name` | String | Required |
| `email` | String | Required and unique |
| `hashed_password` | String | Stored hashed password |
| `role` | String | Defaults to `student` |
| `department_id` | Integer | Foreign key to departments |

### Teacher
| Field | Type | Notes |
| --- | --- | --- |
| `id` | Integer | Primary key |
| `name` | String | Required |
| `email` | String | Required and unique |
| `hashed_password` | String | Stored hashed password |
| `role` | String | Defaults to `teacher` |
| `department_id` | Integer | Foreign key to departments |

## Author
Lalit Kumar  
GitHub: [kumarlalit79](https://github.com/kumarlalit79)
