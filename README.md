# Project Setup and Usage Guide

This guide will walk you through setting up and running the project, as well as running tests.

## Prerequisites

Make sure you have **Python 3** and **pip** installed on your system.

## 1. Set Up a Virtual Environment

To set up a virtual environment for the project, follow these steps:

1. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:

   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

   - On **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```

## 2. Install Dependencies

With the virtual environment activated, install the required project dependencies:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, you can manually install **Django**:

```bash
pip install django
```

## 3. Run Migrations

To set up the database, run the migrations:

```bash
python manage.py migrate
```

## 4. Start the Development Server

To run the development server, use the following command:

```bash
python manage.py runserver
```

You should now be able to access the project at `http://127.0.0.1:8000/` in your browser.

## 5. Running Tests

To run the test suite and ensure that all tests pass, use the following command:

```bash
python manage.py test
```