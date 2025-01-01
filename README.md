# Project Management Application API Documentation

## Overview
This project is a project management application that provides RESTful APIs for managing users, projects, tasks, and comments. The API is built using Django and Django REST Framework.

---
**The project has also been deployed at**
 ```bash
   https://sanketh124.pythonanywhere.com/api/
   ```
---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/sanketh8125/TechForing-Project-Management.git
   ```

2. Navigate to the project directory:
   ```bash
   cd project_management
   ```

3. Install dependencies:
   Make sure you have Python, Django, Django REST Framework installed

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the API at:
   ```
   http://127.0.0.1:8000/api/
   ```

## Database Schema

### Users Table
- **id**: Primary Key
- **username**: String (Unique)
- **email**: String (Unique)
- **password**: String
- **first_name**: String
- **last_name**: String
- **date_joined**: DateTime

### Projects Table
- **id**: Primary Key
- **name**: String
- **description**: Text
- **owner**: Foreign Key (to Users)
- **created_at**: DateTime

### Project Members Table
- **id**: Primary Key
- **project**: Foreign Key (to Projects)
- **user**: Foreign Key (to Users)
- **role**: String (Admin, Member)

### Tasks Table
- **id**: Primary Key
- **title**: String
- **description**: Text
- **status**: String (To Do, In Progress, Done)
- **priority**: String (Low, Medium, High)
- **assigned_to**: Foreign Key (to Users, nullable)
- **project**: Foreign Key (to Projects)
- **created_at**: DateTime
- **due_date**: DateTime

### Comments Table
- **id**: Primary Key
- **content**: Text
- **user**: Foreign Key (to Users)
- **task**: Foreign Key (to Tasks)
- **created_at**: DateTime

---
**The project has also been deployed at**
 ```bash
   https://sanketh124.pythonanywhere.com/api/
   ```
---

# REST API Endpoints

## 1. Users

### 1.1 Register User (POST /api/users/register/)
Create a new user.

**Example URL:**
```
POST /api/users/register/
```

**Request JSON:**
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "password123",
  "first_name": "John",
  "last_name": "Doe"
}
```

**Response JSON:**
```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "date_joined": "2024-12-31T12:00:00Z"
}
```

### 1.2 Login User (POST /api/users/login/)
Authenticate a user and return a token.

**Example URL:**
```
POST /api/users/login/
```

**Request JSON:**
```json
{
  "username": "john_doe",
  "password": "password123"
}
```

**Response JSON:**
```json
{
  "token": "abcd1234efgh5678"
}
```

### 1.3 Get User Details (GET /api/users/{id}/)
Retrieve details of a specific user.

**Example URL:**
```
GET /api/users/1/
```

**Response JSON:**
```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "date_joined": "2024-12-31T12:00:00Z"
}
```

### 1.4 Update User (PUT/PATCH /api/users/{id}/)
Update user details.

**Example URL:**
```
PUT /api/users/1/
```

**Request JSON:**
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "password123",  //optional
  "first_name": "Johnny",
  "last_name": "D",
}
```


```
PATCH /api/users/1/
```

**Request JSON:**
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "password123",  //optional
  "first_name": "Johnny",
  "last_name": "D",
}
```

### 1.5 Delete User (DELETE /api/users/{id}/)
Delete a user account.

**Example URL:**
```
DELETE /api/users/1/
```

---

## 2. Projects

### 2.1 List Projects (GET /api/projects/)
Retrieve a list of all projects.

**Example URL:**
```
GET /api/projects/
```

**Response JSON:**
```json
  {
    "id": 1,
    "name": "Project Alpha",
    "description": "This is the first project.",
    "owner": 1,
    "created_at": "2024-12-31T12:00:00Z"
  }
```

### 2.2 Create Project (POST /api/projects/)
Create a new project.

**Example URL:**
```
POST /api/projects/
```

**Request JSON:**
```json
{
  "name": "Project Alpha",
  "description": "This is the first project.",
  "owner": 1
}
```

**Response JSON:**
```json
{
  "id": 1,
  "name": "Project Alpha",
  "description": "This is the first project.",
  "owner": 1,
  "created_at": "2024-12-31T12:00:00Z"
}
```

### 2.3 Retrieve Project (GET /api/projects/{id}/)
Retrieve details of a specific project.

**Example URL:**
```
GET /api/projects/1/
```

**Response JSON:**
```json
{
    "id": 1,
    "name": "Project Alpha",
    "description": "This is the first project.",
    "owner": 1,
    "created_at": "2024-12-31T12:00:00Z"
  }
```

### 2.4 Update Project (PUT/PATCH /api/projects/{id}/)
Update project details.

**Example URL:**
```
PUT /api/projects/1/
```

**Request JSON:**
```json
{
  "name": "Project Alpha",
  "description": "This is the first project.",
  "owner": 1
}
```

```
PATCH /api/projects/1/
```

**Request JSON:**
```json
{
  "description": "This is the latest project."
}
```

### 2.5 Delete Project (DELETE /api/projects/{id}/)
Delete a project.

**Example URL:**
```
DELETE /api/projects/1/
```

---

## 3. Project Members

### 3.1 List Project Members (GET /api/projectMembers/)
Retrieve a list of all project members.

**Example URL:**
```
GET /api/projectMembers/
```

**Response JSON:**
```json
{
    "id": 1,
    "role": "Member",
    "project": 1,
    "user": 2
}
```

### 3.2 Create Project Members (POST /api/projectMembers/)
Add new project members.

**Example URL:**
```
POST /api/projectMembers/
```

**Request JSON:**
```json
{
    "project": 1,      
    "user": 2,        
    "role": "Member"
}
```

**Response JSON:**
```json
{
    "id": 1,
    "role": "Member",
    "project": 1,
    "user": 2
}
```

### 3.3 Retrieve Project (GET /api/projectMembers/{id}/)
Retrieve details of a specific project member.

**Example URL:**
```
GET /api/projectMembers/1/
```

**Response JSON:**
```json
{
    "id": 1,
    "role": "Member",
    "project": 1,
    "user": 2
}
```

### 3.4 Update Project (PUT/PATCH /api/projects/{id}/)
Update project details.

**Example URL:**
```
PUT /api/projectMembers/1/
```

**Request JSON:**
```json
{
    "role": "Member",
    "project": 1,
    "user": 1
}
```

```
PATCH /api/projectMembers/1/
```

**Request JSON:**
```json
{
    "role": "Admin"
}
```

### 3.5 Delete Project Member (DELETE /api/projectMembers/{id}/)
Deletes a project member.

**Example URL:**
```
DELETE /api/projectMembers/1/
```


---

## 4. Tasks

### 4.1 List Tasks (GET /api/projects/{project_id}/tasks/)
Retrieve a list of all tasks in a project.

**Example URL:**
```
GET /api/projects/1/tasks/
```

**Response JSON:**
```json
   {
        "id": 1,
        "title": "Complete Documentation",
        "description": "Create detailed documentation for the new feature.",
        "status": "To Do",
        "priority": "High",
        "assigned_to": 2,
        "project": 1,
        "created_at": "2024-12-01T10:00:00",
        "due_date": "2024-12-31T23:59:59"
    }
```

### 4.2 Create Task (POST /api/projects/{project_id}/tasks/)
Create a new task in a project.

**Example URL:**
```
POST /api/projects/1/tasks/
```

**Request JSON:**
```json
   {
        "title": "Complete Documentation",
        "description": "Create detailed documentation for the new feature.",
        "status": "To Do",
        "priority": "High",
        "assigned_to": 2,
        "project": 1,
        "due_date": "2024-12-31"
    }
```

### 4.3 Retrieve Task (GET /api/tasks/{id}/)
Retrieve details of a specific task.

**Example URL:**
```
GET /api/tasks/1/
```

**Response JSON:**
```json
   {
        "id": 1,
        "title": "Complete Documentation",
        "description": "Create detailed documentation for the new feature.",
        "status": "To Do",
        "priority": "High",
        "assigned_to": 2,
        "project": 1,
        "created_at": "2024-12-01T10:00:00",
        "due_date": "2024-12-31T23:59:59"
    }
```

### 4.4 Update Task (PUT/PATCH /api/tasks/{id}/)
Update task details.

**Example URL:**
```
PUT /api/tasks/1/
```

**Request JSON:**
```json
{
        "title": "Complete Latest Documentation",
        "description": "Create detailed documentation for the new feature.",
        "status": "To Do",
        "priority": "High",
        "assigned_to": 2,
        "project": 1,
        "due_date": "2024-12-31T23:59:59"
    }
```


```
PATCH /api/tasks/1/
```

**Request JSON:**
```json
{
        "priority": "Low"
    }
```


### 4.5 Delete Task (DELETE /api/tasks/{id}/)
Delete a task.

**Example URL:**
```
DELETE /api/tasks/1/
```

---

## 5. Comments

### 5.1 List Comments (GET /api/tasks/{task_id}/comments/)
Retrieve a list of all comments on a task.

**Example URL:**
```
GET /api/tasks/1/comments/
```

**Response JSON:**
```json
 {
    "id": 1,
    "content": "This task needs more details.",
    "user": 1,
    "task": 1,
    "created_at": "2024-12-31T15:00:00Z"
  }
```

### 5.2 Create Comment (POST /api/tasks/{task_id}/comments/)
Create a new comment on a task.

**Example URL:**
```
POST /api/tasks/1/comments/
```

**Request JSON:**
```json
 {
    "content": "This task needs more details.",
    "user": 1,
    "task": 1
  }
```

### 5.3 Retrieve Comment (GET /api/comments/{id}/)
Retrieve details of a specific comment.

**Example URL:**
```
GET /api/comments/1/
```

**Response JSON:**
```json
   {
    "id": 1,
    "content": "This task needs more details.",
    "user": 1,
    "task": 1,
    "created_at": "2024-12-31T15:00:00Z"
  }
```

### 5.4 Update Comment (PUT/PATCH /api/comments/{id}/)
Update comment details.

**Example URL:**
```
PUT /api/comments/1/
```

**Request JSON:**
```json
{
    "content": "This task needs more latest details.",
    "user": 1,
    "task": 1,
}
```


```
PATCH /api/comments/1/
```

**Request JSON:**
```json
{
    "content": "This task has completed."
}
```



### 5.5 Delete Comment (DELETE /api/comments/{id}/)
Delete a comment.

**Example URL:**
```
DELETE /api/comments/1/
```

---
