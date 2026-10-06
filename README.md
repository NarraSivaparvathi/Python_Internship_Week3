# Task Manager - Django Web Application

## Project Overview

Task Manager is a Django-based web application developed as part of the Week 3 internship task.

The application allows users to register, log in, and manage their personal tasks through a simple web interface.

## Features

- User registration
- User login and logout
- User authentication
- Personal task dashboard
- Create tasks
- View tasks
- Edit tasks
- Delete tasks
- Task status management
- Due date management
- Django admin panel
- SQLite database

## Task Status

Tasks can have one of the following statuses:

- Pending
- In Progress
- Completed

## Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS
- Django Templates

## Project Structure

```text
Python_Internship_Week3/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── tasks/
│   ├── migrations/
│   ├── templates/
│   │   └── tasks/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
