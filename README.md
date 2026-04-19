## Flask Book Library with SQLite

This project is a Flask web application that allows users to add and view books along with their author and rating.

Unlike previous file-based storage approaches, this application uses SQLite with SQLAlchemy ORM to store and manage data in a structured and scalable way.

Users can add books through a form, and all records are stored in a database and displayed dynamically on the homepage.

This project was built as part of the #90DaysOfCode challenge to practice database integration, ORM usage, and backend data handling using Flask.

---

## Technologies Used

Python  
Flask  
Flask-SQLAlchemy  
SQLite  
HTML5  
Jinja2 Templating  

---

## Key Concepts Demonstrated

Database integration using SQLite

Using SQLAlchemy ORM for data modeling

Creating database tables programmatically

Handling form submissions with Flask

Validating user input (rating constraints)

Storing and retrieving structured data

Rendering database records dynamically

---

## Project Structure

```
project/
│
├── main.py
├── books.db
│
├── templates/
│   ├── index.html
│   └── add.html
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/faizhsnnn/flask-book-library-sqlite.git
cd flask-book-library-sqlite
```

---

### 2. Create a virtual environment

```
python -m venv venv
```

Activate it:

**Windows**
```
venv\Scripts\activate
```

**Mac/Linux**
```
source venv/bin/activate
```

---

### 3. Install dependencies

```
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

### 4. Python Version

This project is recommended to run on:

Python 3.10 or above

(Some environments may require Python 3.10–3.12 for compatibility with Flask and SQLAlchemy versions.)

---

### 5. Run the application

```
python main.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## Application Workflow

1. User opens homepage
2. Existing books are fetched from SQLite database
3. User navigates to add book page
4. Submits book details (title, author, rating)
5. Flask validates rating input
6. Data is stored in the database using SQLAlchemy
7. User is redirected to homepage
8. Updated list is displayed

---

## Why This Project Matters

This project demonstrates the transition from simple file storage to database-driven applications.

It introduces:

Structured data storage  
ORM-based database interaction  
Scalable backend design  

These are core concepts used in real-world backend systems.

---

## Author

Faiz Hasan  
Python Automation & Backend Developer
