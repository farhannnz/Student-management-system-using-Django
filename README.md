# Student Management System

## Overview
The **Student Management System** is a web-based application built with **Django** that allows administrators, teachers, and students to manage student-related information efficiently. The system provides role-based access where:
- **Admins** can manage students, teachers, subjects, and courses.
- **Teachers** can manage attendance and student marks for their assigned subjects.
- **Students** can view their marks, attendance, and other academic details.

## Features
### **Admin Panel**
- Create, update, and delete **students, teachers, courses, and subjects**.
- Assign subjects to teachers.
- View and manage attendance records.
- Generate student performance reports.
- Manage user authentication and permissions.

### **Student Dashboard**
- View personal academic details.
- Check **attendance percentage** and subject-wise attendance.
- View **exam marks** and internal assessment scores.
- Receive notifications for upcoming exams and low attendance.

## Technologies Used
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Database:** SQLite (can be switched to PostgreSQL/MySQL)
- **Authentication:** Django’s built-in authentication system

## Installation & Setup
### **Prerequisites**
Ensure you have Python installed (Recommended: Python 3.8+).

### **Step 1: Clone the Repository**
```sh
git clone https://github.com/farhannnz/Student-management-system-using-Django.git
cd Student-management-system-using-Django
```

### **Step 2: Create a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate  # For Windows
```

### **Step 3: Install Dependencies**
```sh
pip install -r requirements.txt
```

### **Step 4: Apply Migrations**
```sh
python manage.py makemigrations
python manage.py migrate
```

### **Step 5: Create a Superuser (Admin Access)**
```sh
python manage.py createsuperuser
```
Follow the prompts to set up an admin username and password.

### **Step 6: Run the Development Server**
```sh
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

## Usage
1. **Admin Login:** Use the superuser credentials to access the Django admin panel at `http://127.0.0.1:8000/admin/`.
2. **Teacher Login:** Teachers can log in and manage student marks and attendance.
3. **Student Login:** Students can log in to view their academic records.

## Screenshots
(Add screenshots of the admin panel, teacher dashboard, and student dashboard here.)

## Future Enhancements
- Implement role-based dashboards with React.js.
- Add email notifications for students about attendance and marks.
- Integrate an AI-based student performance prediction system.
- Add an API for mobile app integration.

