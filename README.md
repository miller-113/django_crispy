# Django Project Setup Guide

## Prerequisites
Make sure you have the following installed:
- Python (>=3.8 recommended)
- pip (Python package manager)
- virtualenv (optional but recommended)

## Installation Steps

### 1. Clone the Repository (if applicable)
```sh
cd django_forms
```

### 2. Create a Virtual Environment (Recommended)
```sh
python -m venv venv
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Set Up the Django Project
#### a) Apply Migrations
```sh
python manage.py migrate
```

#### b) Create a Superuser (Optional, for Admin Access)
```sh
python manage.py createsuperuser
```

### 5. Run the Development Server
```sh
python manage.py runserver
```

Now, open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.
