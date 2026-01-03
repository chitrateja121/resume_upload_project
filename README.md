# Resume Upload Web Application (Django + MySQL)

This is a web-based **Resume Upload Portal** developed using **Django, Python, and MySQL**.  
The application allows users to upload and store resumes through a simple web interface.  
Uploaded resumes are saved securely on the server and corresponding user records are stored in the database.

This project was built to practice full-stack web development and learn how file uploads work in Django.

---

## 🚀 Features

✔ Upload resumes (PDF / DOC / etc.)  
✔ Store uploaded files securely  
✔ Save user data in MySQL  
✔ Simple and clean UI  
✔ Django backend with ORM  
✔ Form handling & validation  

---

## 🛠 Technologies Used

- Python  
- Django Framework  
- MySQL Database  
- HTML / CSS  
- Bootstrap (optional)

---

## 📂 Project Structure (Simple View)


---

## ⚙️ Setup Instructions

Follow these steps to run the project locally.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/chitrateja121/resume_upload_project.git
```
### 2️⃣ Open the Project Folder
```
cd resume_upload_project
```
### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
### 4️⃣ Configure MySQL in settings.py
```
DATABASES = {
 'default': {
   'ENGINE': 'django.db.backends.mysql',
   'NAME': 'resume_db',
   'USER': 'root',
   'PASSWORD': '',
   'HOST': 'localhost',
   'PORT': '3306',
 }
}
```
### 5️⃣ Apply Database Migrations
```
python manage.py migrate
```
### 6️⃣ Run the Development Server
```
python manage.py runserver
```
### 7️⃣ Open the Application in Browser
```
http://127.0.0.1:8000/
```

