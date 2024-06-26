# Overview

#  Welcome to Attendance_System

## Attendance_System is a Django web application designed to the Attendance System simplifies school and college operations by centralizing student details, attendance tracking, grade recording, and teacher information, all in one platform.

## Features
### Student Management:
 Keep track of student details like names and contact info.
### Attendance Management:
 Record who's present and who's absent in class.
### Grade Management:
 Keep track of student grades for different assignments and
exams.
### Teacher Management:
 Keep a record of teachers, what subjects they teach, and how to
contact them.
### Communication Tools:

 Provide ways for teachers to communicate with students and vice
versa.

## Installation
### 1.Clone the Repository:
   ```bash
   git clone https://github.com/Dillibabu2357/Attendance_System.git
   ```
### 2.change directory:
```bash
cd Attendance_system
```

### 3.Create virtual Environment:
```bash
python -m venv venv
```

 ### 4.Activate:
 ```bash
venv\Scripts\activate
```

### 5.Install Dependencies:
***Install Django:*** First, you need to install Django using pip. Make sure you have Python installed on your system.

```bash
pip install django
```

### 6.Run migrations:
```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

### 7.Create a superuser account:

```bash
python manage.py createsuperuser
```

### 8. Run the surver:
```bash
python manage.py runserver
```

### 9.Admin-panel found at:
```bash
 http://127.0.0.1:8000/admin/
```

### 10.To Run the Unit-tests:

```bash
 python manage.py test -v 2
```



