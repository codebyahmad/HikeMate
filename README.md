![MasterHead](https://i.postimg.cc/85C5Ygt4/Hike-Logo.png)

# HikeMate - A Trail Recommender System

developed by M.Sc. Information Systems students from the University of Münster.

Data Integration - Capstone Project - December 2023

## Overview

HikeMate is a trail recommender system that provides personalized trail recommendations in Switzerland.

## Data Collection and Cleaning

Our Trail Recommender System relies on trail data scraped from [AllTrails](https://www.alltrails.com), specifically focusing on Switzerland. We've set up a standalone Python project, [alltrails](./alltrails/), which scrapes the AllTrails JSON API.

## How to run it

Before you begin, ensure that you have the following installed on your machine:

- [Python](https://www.python.org/) (3.6 or higher)
- [pip](https://pip.pypa.io/en/stable/) (Python package installer)
- [PostgreSQL](https://www.postgresql.org/) (Database server)

## Setting up a Virtual Environment

1. Install Virtual Environment

   ```bash
   pip install virtualenv
   ```

2. Create Virtual Environment
   ```bash
   python -m virtualenv venv
   ```
3. Activate Virutal Environment

   On Windows:

   ```bash
   venv\Scripts\activate
   ```

   On Mac:

   ```bash
   source venv/bin/activate
   ```

_To stop the virtual environment, type **deactivate** in the command prompt._

4. Navigate to Project Folder

   ```bash
   cd backend
   ```

5. Install dependencies
   ```bash
   pip install requirements.txt
   ```
   
## Setting up Database

1. Ensure that PostgreSQL is installed and running.
2. Create a PostgreSQL database for your Django project.
3. Update the DATABASE setting in `core/settings.py`:
   ```bash
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_database_name',
            'USER': 'your_database_user',
            'PASSWORD': 'your_database_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```
   Replace **your_database_name**, **your_database_user**, and **your_database_password** with your actual database information.

4. Make migrations and apply them:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## Run the development server

1. Start the development server:
   ```bash
   python manage.py runserver
   ```
2. Open your web browser and navigate to http://127.0.0.1:8000/ to view the application.

_To stop the development server, press Ctrl + C in the command prompt._

## Creating a Superuser (Admin)

To access the Django admin interface, you need to create a superuser account:

1. Run the following command:
   ```bash
   python manage.py createsuperuser
   ```
2. Follow the prompts to enter a username, email, and password.
3. Access the admin interface at http://127.0.0.1:8000/admin/ and log in using the superuser credentials.

## Authors

- Asad Mahmood Ahmad ([@codebyahmad](https://github.com/codebyahmad))
- Alisher Nosirov ([@temptationofhiphop](https://github.com/temptationofhiphop))
- Nail Khazeev ([@Naill23](https://github.com/Naill23))
- Isroil Khudoyberdiev

Enjoy using it! 🚵🏽‍♂️ 🌍