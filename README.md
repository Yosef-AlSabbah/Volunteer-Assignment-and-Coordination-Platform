# Volunteer Assignment and Coordination Platform

A comprehensive web application for volunteer coordination and management, designed to efficiently assign volunteers to specific tasks at different workplaces such as hospitals, aid distribution centers, and more.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [API Documentation](#api-documentation)
  - [Authentication](#authentication)
  - [Workplaces Management](#workplaces-management)
  - [Tasks Management](#tasks-management) 
  - [Volunteers Management](#volunteers-management)
  - [Assignment of Volunteers](#assignment-of-volunteers)
- [Project Structure](#project-structure)
- [Development](#development)
- [Deployment](#deployment)
- [About](#about)

## Overview

The Volunteer Assignment and Coordination Platform is designed to streamline the process of managing volunteers and assigning them to specific tasks at different workplaces. The platform features a secure admin interface for managing all operations with no public user registration.

## Features

- **Authentication**: Secure login and logout for admin users
- **Workplaces Management**: Add, edit, delete, and view workplaces
- **Tasks Management**: Create and manage tasks linked to specific workplaces
- **Volunteers Management**: Register, update, and track volunteer information
- **Assignments**: Assign volunteers to specific workplace tasks
- **Standardized API Responses**: Consistent response format across all endpoints
- **Comprehensive Documentation**: Detailed API documentation using Swagger/OpenAPI

## Technology Stack

- **Backend Framework**: Django 5.2 with Django REST Framework
- **Authentication**: Djoser and Simple JWT
- **Database**: PostgreSQL
- **Caching**: Redis
- **API Documentation**: drf-spectacular (Swagger/OpenAPI)
- **Containerization**: Docker & Docker Compose
- **CORS Handling**: django-cors-headers

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Git (for version control)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/volunteer-assignment-and-coordination-platform.git
   cd volunteer-assignment-and-coordination-platform
   ```

2. Create a `.env` file in the root directory with the following variables:
   ```
   POSTGRES_DB=volunteer_platform_db
   POSTGRES_USER=admin
   POSTGRES_PASSWORD=admin_password
   DB_HOST=db
   DB_PORT=5432
   
   REDIS_HOST=redis
   REDIS_PORT=6379
   
   DJANGO_SECRET_KEY=your-secret-key
   DJANGO_DEBUG=True
   DJANGO_ALLOWED_HOSTS='["localhost", "127.0.0.1"]'
   ```

3. Build and start the Docker containers:
   ```bash
   docker-compose up -d
   ```

4. Run migrations to set up the database:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. Create a superuser (admin):
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

6. Access the API at http://localhost:8000/

## API Documentation

Access the API documentation at `/api/schema/swagger-ui/` or `/api/schema/redoc/`

### Authentication

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/auth/jwt/create/` | POST | Obtain JWT token for authentication |
| `/api/auth/jwt/refresh/` | POST | Refresh JWT token |
| `/api/auth/jwt/verify/` | POST | Verify JWT token validity |
| `/api/auth/users/` | GET | List all users (admin only) |
| `/api/auth/users/` | POST | Create a new user (admin only) |
| `/api/auth/users/{id}/` | GET | Get user details (admin only) |
| `/api/auth/users/{id}/` | PUT/PATCH | Update user (admin only) |
| `/api/auth/users/{id}/` | DELETE | Delete user (admin only) |
| `/api/auth/users/me/` | GET | Get current user details |
| `/api/auth/users/me/` | PUT/PATCH | Update current user |
| `/api/auth/users/me/` | DELETE | Delete current user |
| `/api/auth/users/set_password/` | POST | Change password |

### Workplaces Management

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/workplaces/` | GET | List all workplaces |
| `/api/workplaces/` | POST | Create a new workplace |
| `/api/workplaces/{id}/` | GET | Retrieve workplace details |
| `/api/workplaces/{id}/` | PUT/PATCH | Update workplace information |
| `/api/workplaces/{id}/` | DELETE | Delete a workplace |

### Tasks Management

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/tasks/` | GET | List all tasks |
| `/api/tasks/` | POST | Create a new task |
| `/api/tasks/{id}/` | GET | Retrieve task details |
| `/api/tasks/{id}/` | PUT/PATCH | Update task information |
| `/api/tasks/{id}/` | DELETE | Delete a task |

### Volunteers Management

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/volunteers/` | GET | List all volunteers |
| `/api/volunteers/` | POST | Register a new volunteer |
| `/api/volunteers/{id}/` | GET | Retrieve volunteer details |
| `/api/volunteers/{id}/` | PUT/PATCH | Update volunteer information |
| `/api/volunteers/{id}/` | DELETE | Remove a volunteer |

### Assignment of Volunteers

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/assignments/` | GET | List all assignments |
| `/api/assignments/` | POST | Create a new assignment |
| `/api/assignments/{id}/` | GET | Retrieve assignment details |
| `/api/assignments/{id}/` | PUT/PATCH | Update an assignment |
| `/api/assignments/{id}/` | DELETE | Delete an assignment |

## Project Structure

```
volunteer_platform/
├── core/                 # Core application with models and views
├── volunteer_platform/   # Project settings and configuration
│   ├── core/             # Core utilities for API responses
│   │   ├── api_standard_response.py
│   │   ├── exceptions.py
│   │   ├── mixins.py
│   │   └── renderers.py
│   └── utils/            # Utility modules
│       └── pagination.py
├── docker-compose.yml    # Docker Compose configuration
├── Dockerfile            # Docker build instructions
├── manage.py             # Django management script
├── pyproject.toml        # Project dependencies
└── README.md             # Project documentation
```

## Development

### Running Tests
```bash
docker-compose exec web python manage.py test
```

### Code Style
This project follows PEP 8 guidelines for Python code.

## Deployment

For production deployment, consider:

1. Setting `DEBUG=False` in your environment variables
2. Using a secure `SECRET_KEY`
3. Configuring `ALLOWED_HOSTS` appropriately
4. Setting up HTTPS with a valid SSL certificate
5. Properly configuring static files serving

## About

**Project**: Volunteer Assignment and Coordination Platform  
**Course**: Web 3  
**Instructor**: Mohammed Al-Agha  
**Student**: Yousef M. Y. Al Sabbah  
**Student ID**: 120212265  

---

© 2025 Yousef M. Y. Al Sabbah
