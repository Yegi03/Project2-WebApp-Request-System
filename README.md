# Maintenance Request Web Application


## Overview

The Maintenance Request Web Application is a Python-based project built with Flask that enables tenants, staff, and managers to efficiently manage apartment maintenance requests. Tenants can submit requests for repairs, staff can browse and update requests, and managers can handle tenant records.

## Features

- **Submit Maintenance Requests:** Tenants can submit requests with details like apartment number, problem area, description, and an optional photo. Requests are automatically assigned a unique ID and marked as "pending."
- **Browse and Filter Requests:** Staff can view all requests and filter them by apartment number, problem area, date range, and status.
- **Manage Tenant Accounts:** Managers can add, move, and delete tenant accounts with details like name, phone number, email, and apartment number.
- **Technologies Used

## Technologies Used
- **Backend:** Flask (Python3)
- **Database:** SQLite
- **Frontend:** HTML, CSS

  

## Project Structure

- **maintenance-request-webapp/**
  - `main.py`: Core Flask application and routes
  - `config.py`: Application configuration and database URI
  - `models.py`: SQLAlchemy models for Tenant and MaintenanceRequest
  - `requirements.txt`: Python dependencies
  - **instance/**
    - `maintenance.db`: SQLite database file
  - **templates/**
    - **tenant/**
      - `dashboard.html`: Tenant dashboard view
      - `submit_request.html`: Form to submit a maintenance request
      - `request_success.html`: Confirmation page for submitted requests
    - **staff/**
      - `dashboard.html`: Staff dashboard view
      - `browse_requests.html`: Page for browsing and filtering requests
    - **manager/**
      - `dashboard.html`: Manager dashboard view
  - **static/**
    - **css/**
      - `styles.css`: Main stylesheet
  - `README.md`: This file
  - `.gitignore`: Git ignore file to exclude unnecessary files


## Setup and Installation

### Prerequisites

- **Python 3.6+**: Ensure Python 3.6 or higher is installed. If not, download and install from [Python.org](https://www.python.org/downloads/).
- **Flask and SQLAlchemy**: These libraries are needed to run the application and are included in the `requirements.txt`.

### Step-by-Step Guide

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yegi03/maintenance-request-webapp.git
   cd maintenance-request-webapp

2.  **Set Up a Virtual Environment**:

  python -m venv .venv
  source .venv/bin/activate  # For macOS/Linux
  .venv\Scripts\activate      # For Windows


3. **Install Dependencies**:
```bash
  pip install -r requirements.txt
  Configure the Database: Make sure the config.py file contains the correct path to the database:
  SQLALCHEMY_DATABASE_URI = "sqlite:///instance/maintenance.db"



4. **Initialize the Database** :
python
Then run the following commands in the Python shell:

from main import app, db
with app.app_context():
    db.create_all()
exit()
Run the Application:
flask run
Usage

Tenant Actions
Submit Maintenance Request: Tenants can submit a request with the problem details and an optional photo attachment.
Staff Actions
Browse Requests: Staff can view and filter requests by apartment, problem area, date, or status.
Update Status: Staff can mark a request as "completed" once resolved.
Manager Actions
Manage Tenants: Managers can add, move, or delete tenants within the system.
Database Structure

This application uses an SQLite database with the following tables:

Tenants Table: Contains tenant ID, name, phone, email, apartment number, check-in, and check-out dates.
MaintenanceRequests Table: Stores each maintenance request, including request ID, apartment number, problem area, description, submission date, optional photo, and status.
GitHub Deployment

Initialize the Repository:
git init
git add .
git commit -m "Initial commit"
Create a GitHub Repository: Go to GitHub and create a new repository.
Add Remote and Push: Replace YourUsername and RepositoryName with your GitHub username and repository name.
git remote add origin https://github.com/YourUsername/RepositoryName.git
git push -u origin main
License

This project is open-source and available under the MIT License.
