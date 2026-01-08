# FastAPI User Management Application

A simple REST API built with FastAPI for managing users. This application allows you to create, read, update, and delete users with name and email information.

## Table of Contents

1. [What is This Project?](#what-is-this-project)
2. [Prerequisites](#prerequisites)
3. [Technology Stack](#technology-stack)
4. [Project Setup](#project-setup)
5. [Project Structure](#project-structure)
6. [Running the Application](#running-the-application)
7. [Using the API](#using-the-api)
8. [Troubleshooting](#troubleshooting)

---

## What is This Project?

This is a **REST API** (Application Programming Interface) built with FastAPI. Think of it as a web service that allows applications to:

- **Create** new users
- **Read/Get** all users or specific users
- **Update** existing users
- **Delete** users

It uses a SQLite database to store user information (name and email).

---

## Prerequisites

Before you begin, make sure you have the following installed on your computer:

### 1. Python 3.8 or Higher

**How to Check:**

- Open Command Prompt (Windows) or Terminal (Mac/Linux)
- Type: `python --version` or `python3 --version`
- You should see something like `Python 3.8.x` or higher

**How to Install Python:**

1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download the latest Python version for your operating system
3. Run the installer
4. **Important:** Check the box "Add Python to PATH" during installation
5. Follow the installation wizard

### 2. pip (Python Package Installer)

pip usually comes with Python. Verify it's installed:

```bash
pip --version
```

If it's not installed, you'll need to reinstall Python with the "Add Python to PATH" option checked.

---

## Technology Stack

Don't worry if these terms are new! Here's what each technology does:

| Technology     | What It Does                                                                                             |
| -------------- | -------------------------------------------------------------------------------------------------------- |
| **FastAPI**    | The web framework that handles HTTP requests and responses (like a waiter in a restaurant taking orders) |
| **SQLAlchemy** | A toolkit that lets Python talk to databases (like a translator between Python and SQL)                  |
| **SQLite**     | A simple file-based database (stores data in a file on your computer)                                    |
| **Pydantic**   | Validates data to make sure it's in the correct format (like checking if an email looks like an email)   |
| **Uvicorn**    | The server that runs your FastAPI application (the engine that makes everything work)                    |

---

## Project Setup

### Step 1: Clone or Download the Project

If you have the project files, navigate to the project folder. If you're using Git:

```bash
cd fast_api
```

### Step 2: Create a Virtual Environment (Recommended)

A virtual environment keeps your project's dependencies separate from other Python projects.

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

When activated, you'll see `(venv)` at the beginning of your command prompt.

**To deactivate later:** Just type `deactivate`

### Step 3: Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

This will install all the packages listed in `requirements.txt` (FastAPI, SQLAlchemy, etc.).

### Step 4: Create Environment File

Create a file named `.env` in the project root (same folder as `requirements.txt`):

**Windows (PowerShell):**

```bash
New-Item .env
```

**Mac/Linux:**

```bash
touch .env
```

Then open `.env` and add:

```
APP_NAME=FastAPI User Management
DEBUG=True
```

### Step 5: Verify Setup

Check if everything is installed correctly:

```bash
python -c "import fastapi; print('FastAPI installed successfully!')"
```

---

## Project Structure

Here's what each folder and file does:

```
fast_api/
│
├── app/                    # Main application folder
│   ├── api/               # API routes (endpoints)
│   │   └── routes/
│   │       ├── health.py  # Health check endpoint (/health)
│   │       └── users.py   # User CRUD operations (/users)
│   │
│   ├── core/              # Core settings
│   │   └── config.py      # Application configuration
│   │
│   ├── db/                # Database related files
│   │   ├── base.py        # Base class for database models
│   │   └── session.py     # Database connection setup
│   │
│   ├── models/            # Database models (table structures)
│   │   └── user.py        # User table definition
│   │
│   ├── schemas/           # Data validation schemas
│   │   └── user.py        # User data formats (create/response)
│   │
│   └── main.py            # Application entry point
│
├── app.db                 # SQLite database file (created automatically)
├── requirements.txt       # Python dependencies list
└── README.md             # This file!
```

**Simple Explanation:**

- **models/** = Defines what data looks like in the database (like a blueprint)
- **schemas/** = Defines what data should look like when sent/received via API
- **routes/** = Defines the URLs and what happens when you visit them
- **db/** = Handles database connections
- **main.py** = Starts the application

---

## Running the Application

### Start the Server

In your terminal (with virtual environment activated), run:

```bash
uvicorn app.main:app --reload
```

**What this command does:**

- `uvicorn` = The server program
- `app.main:app` = Location of your FastAPI application
- `--reload` = Automatically restart server when code changes (great for development!)

You should see output like:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Access the Application

1. **API Documentation (Interactive):**

   - Open your browser and go to: `http://127.0.0.1:8000/docs`
   - This shows a beautiful, interactive API documentation where you can test all endpoints!

2. **Alternative Documentation:**

   - Go to: `http://127.0.0.1:8000/redoc`
   - Alternative documentation format

3. **Health Check:**
   - Go to: `http://127.0.0.1:8000/health`
   - Should return: `{"status": "ok", "message": "Service is healthy"}`

### Stop the Server

Press `CTRL + C` in your terminal.

---

## Using the API

### Method 1: Using the Interactive Docs (Easiest!)

1. Go to `http://127.0.0.1:8000/docs` in your browser
2. You'll see all available endpoints
3. Click on any endpoint to expand it
4. Click "Try it out"
5. Fill in the required information
6. Click "Execute"
7. See the response below

### Method 2: Using cURL (Command Line)

**Create a User:**

```bash
curl -X POST "http://127.0.0.1:8000/users/" -H "Content-Type: application/json" -d "{\"name\":\"John Doe\",\"email\":\"john@example.com\"}"
```

**Get All Users:**

```bash
curl -X GET "http://127.0.0.1:8000/users/"
```

**Update a User (replace `1` with actual user ID):**

```bash
curl -X PUT "http://127.0.0.1:8000/users/1" -H "Content-Type: application/json" -d "{\"name\":\"Jane Doe\"}"
```

**Delete a User (replace `1` with actual user ID):**

```bash
curl -X DELETE "http://127.0.0.1:8000/users/1"
```

### Method 3: Using Python requests Library

Create a file `test_api.py`:

```python
import requests

# Create a user
response = requests.post(
    "http://127.0.0.1:8000/users/",
    json={"name": "John Doe", "email": "john@example.com"}
)
print("Created:", response.json())

# Get all users
response = requests.get("http://127.0.0.1:8000/users/")
print("All users:", response.json())
```

Run it:

```bash
pip install requests
python test_api.py
```

### Available Endpoints

| Method | Endpoint           | Description             | Body Required?          |
| ------ | ------------------ | ----------------------- | ----------------------- |
| GET    | `/health`          | Check if API is running | No                      |
| GET    | `/users/`          | Get all users           | No                      |
| POST   | `/users/`          | Create a new user       | Yes (name, email)       |
| PUT    | `/users/{user_id}` | Update a user           | Yes (name and/or email) |
| DELETE | `/users/{user_id}` | Delete a user           | No                      |

**Example Request Body for POST/PUT:**

```json
{
  "name": "John Doe",
  "email": "john@example.com"
}
```

---

## Troubleshooting

### Problem: "python: command not found" or "python3: command not found"

**Solution:** Python is not installed or not in PATH. Reinstall Python and make sure to check "Add Python to PATH".

### Problem: "pip: command not found"

**Solution:** pip is not installed. Reinstall Python or try `python -m pip` instead of just `pip`.

### Problem: "ModuleNotFoundError: No module named 'fastapi'"

**Solution:** You haven't installed dependencies. Run `pip install -r requirements.txt` again. Make sure your virtual environment is activated.

### Problem: "Address already in use"

**Solution:** Port 8000 is already in use. Either:

- Stop the other application using port 8000
- Or use a different port: `uvicorn app.main:app --reload --port 8001`

### Problem: "No such file or directory: .env"

**Solution:** Create the `.env` file as described in Step 4 of Project Setup.

### Problem: "Database is locked" (SQLite error)

**Solution:** Another process is using the database. Make sure only one instance of the server is running. You can also delete `app.db` to start fresh (all data will be lost).

### Problem: Virtual environment won't activate

**Windows PowerShell:** If you get an error about execution policy, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## Next Steps

Now that you have the application running:

1. **Explore the Interactive Docs:** Visit `http://127.0.0.1:8000/docs` and try creating, reading, updating, and deleting users
2. **Read the Code:** Start with `app/main.py` and follow how requests flow through the application
3. **Modify and Experiment:** Try adding new fields to the User model or creating new endpoints
4. **Learn More:**
   - [FastAPI Documentation](https://fastapi.tiangolo.com/)
   - [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

---

## Quick Reference Commands

```bash
# Activate virtual environment (Windows)
venv\Scripts\activate

# Activate virtual environment (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload

# Deactivate virtual environment
deactivate
```

---

## Support

If you encounter any issues not covered here:

1. Check that all prerequisites are installed correctly
2. Verify your `.env` file exists and has correct content
3. Make sure your virtual environment is activated
4. Try deleting `app.db` and restarting the server (this will recreate the database)

Happy coding! 🚀
