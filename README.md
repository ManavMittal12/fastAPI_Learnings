# ⚡ FastAPI - The Complete Course (Beginner + Advanced)

> Learning repository tracking progress, project builds, and notes for the Udemy course: [FastAPI - The Complete Course](https://www.udemy.com/course/fastapi-the-complete-course/) by Eric Roby & Chad Darby.

---

## 📊 Course Progress Overview

- **Total Sections:** 17
- **Completed:** 0 / 17
- **Status:** In Progress 🚀



[░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0% Completed


---

## 🗂️ Curriculum & Progress Checklist

<details open>
<summary><b>Part 1: Setup & Python Essentials</b></summary>

- [ ] **Section 1: Introduction**
  - [ ] Course overview and prerequisites
  - [ ] Setting up the learning environment
- [ ] **Section 2: Python Installation & Refresher**
  - [ ] Python installation and virtual environments (`venv`)
  - [ ] Python syntax refresher (variables, data types, functions)
  - [ ] OOP concepts in Python
- [ ] **Section 3: FastAPI Overview**
  - [ ] Why FastAPI? (Speed, Starlette, Pydantic)
  - [ ] Automatic API documentation (Swagger UI & ReDoc)
- [ ] **Section 4: FastAPI Setup & Installation**
  - [ ] Installing FastAPI and `uvicorn`
  - [ ] First "Hello World" endpoint & ASGI server reload

</details>

<details open>
<summary><b>Part 2: Core Fundamentals & CRUD APIs</b></summary>

- [ ] **Section 5: Project 1 – FastAPI Request Method Logic**
  - [ ] Setting up initial endpoints
  - [ ] Path parameters and Query parameters
  - [ ] HTTP Methods: `GET`, `POST`, `PUT`, `DELETE`
- [ ] **Section 6: Project 2 – Move Fast with FastAPI (Books Project)**
  - [ ] Pydantic models and request validation
  - [ ] Field constraints, defaults, and typing
  - [ ] HTTP status codes handling & custom error exceptions
  - [ ] Response models and schema filtering

</details>

<details open>
<summary><b>Part 3: Databases & Security (Todo App)</b></summary>

- [ ] **Section 7: Project 3 – Complete RESTful APIs (Setup Database)**
  - [ ] Introduction to ORMs & SQLAlchemy setup
  - [ ] SQLite database connection & session configuration
  - [ ] Creating models and database schemas
- [ ] **Section 8: API Request Methods with Database**
  - [ ] Implementing database CRUD operations
  - [ ] Dependency Injection (`Depends`) for DB sessions
  - [ ] Handling entity relationships
- [ ] **Section 9: Authentication & Authorization**
  - [ ] Password hashing with `bcrypt` / `passlib`
  - [ ] OAuth2 password bearer flow
  - [ ] Generating and decoding JSON Web Tokens (JWT)
- [ ] **Section 10: Authenticate Requests**
  - [ ] Protecting endpoints via JWT dependencies
  - [ ] User role verification and permission scopes
- [ ] **Section 11: Large Production Database Setup**
  - [ ] Migrating from SQLite to PostgreSQL / MySQL
  - [ ] Production connection pooling and configuration

</details>

<details open>
<summary><b>Part 4: Advanced Tooling & Production Engineering</b></summary>

- [ ] **Section 12: Project 3.5 – Alembic Data Migrations**
  - [ ] Initializing and configuring Alembic
  - [ ] Generating and running automated migration scripts
  - [ ] Rollbacks and schema versioning
- [ ] **Section 13: Project 4 – Unit & Integration Testing**
  - [ ] Setting up `pytest` and `TestClient`
  - [ ] Mocking database sessions with test databases
  - [ ] Writing end-to-end tests for secured endpoints
- [ ] **Section 14: Project 5 – Full Stack Application**
  - [ ] Serving Jinja2 HTML templates via FastAPI
  - [ ] Static files configuration (CSS/JS)
  - [ ] Form handling and session cookie authentication

</details>

<details>
<summary><b>Part 5: Version Control, Deployment & Archival</b></summary>

- [ ] **Section 15: Git – Version Control**
  - [ ] Git workflow for FastAPI projects
  - [ ] `.gitignore` best practices for Python/FastAPI
- [ ] **Section 16: Deploying FastAPI Applications**
  - [ ] Environment variables & `.env` secrets management
  - [ ] Production deployment (e.g., Render, Railway, AWS, or Docker)
- [ ] **Section 17: Summary & Wrap-Up**
  - [ ] Course review & next steps
- [ ] *(Optional / Legacy) Section 18: FastAPI < 0.100.0 Full Stack Application*

</details>

---

## 🛠️ Tech Stack & Key Libraries

- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **ASGI Server:** [Uvicorn](https://www.uvicorn.org/)
- **Data Validation:** [Pydantic](https://docs.pydantic.dev/)
- **ORM / Migrations:** [SQLAlchemy](https://www.sqlalchemy.org/) & [Alembic](https://alembic.sqlalchemy.org/)
- **Authentication:** OAuth2 with Password Flow + JWT (`python-jose` / `pyjwt`, `passlib`, `bcrypt`)
- **Testing:** `pytest` + `httpx` (`TestClient`)
- **Templates:** `Jinja2`

---

## 📁 Repository Structure

```text
├── project-1-basics/       # Basic HTTP request endpoints
├── project-2-books/        # Pydantic validation & schemas
├── project-3-todo-app/     # Full REST API with DB, JWT Auth & Alembic
├── project-4-testing/      # Pytest suites and integration tests
├── project-5-fullstack/    # Jinja2 templates & frontend integration
└── README.md