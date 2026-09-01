# Django Learning Journey

The goal of this repository is to document my progress from basic environment setup to building dynamic, database-driven web applications and scalable APIs using Django's MVT (Model-View-Template) architecture.

---

## 🚀 What I Am Learning

I am mastering backend web development. 
The journey progresses logically through the following stages:

1. **Foundation & Architecture:** Setting up isolated Python environments, understanding the request-response cycle, and the MVT design pattern.
2. **Modularity & Routing:** Building isolated "Apps," mapping dynamic URLs, and passing parameters through views.
3. **Frontend Integration:** Utilizing Django Template Language (DTL), managing static files, and integrating frameworks like Bootstrap.
4. **Database Management (ORM):** Interacting with databases using Python instead of raw SQL, and mastering QuerySets to retrieve, filter, and manipulate data.
5. **Admin & CMS:** Customizing the built-in Django Admin interface for robust content management.
6. **Advanced Concepts:** Handling forms, processing file and image uploads, and understanding the request middleware lifecycle.
7. **APIs:** Transitioning to modern backend architecture using the Django REST Framework (DRF).

---

## 📚 Concepts Covered

### 1. Environment & Project Setup

* **Virtual Environments:** Isolating project dependencies using `virtualenv` to prevent version conflicts.
* **Project Architecture:** Understanding the difference between *Projects* (the container) and *Apps* (the modules).
* **Core Commands:** `startproject`, `startapp`, and `runserver`.
* **Folder Structure:** Roles of `manage.py`, `settings.py`, `urls.py`, `views.py`, and `wsgi/asgi.py`.

### 2. Views & URLs (Routing)

* **Functional Views:** Writing Python functions in `views.py` that return an `HttpResponse`.
* **Modular Routing:** Using `include()` to forward requests from the main project to app-specific URL configurations.
* **Dynamic Parameters:** Capturing data from URLs using `<int:id>`, `<str:name>`, `re_path()` (regex), and Python `**kwargs`.

### 3. Templates & Frontend Integration

* **Template Setup:** Configuring project-level and app-level `templates` directories.
* **Template Inheritance:** Using `{% block content %}` and `{% extends 'base.html' %}` for DRY (Don't Repeat Yourself) HTML design.
* **Static Files:** Serving CSS, JavaScript, and Images in development.
* **Bootstrap Integration:** Injecting Bootstrap components directly into Django templates for rapid UI development.

### 4. Database & ORM (Object Relational Mapping)

* **Models:** Defining database tables using Python classes in `models.py`.
* **Migrations:** Creating and applying schema changes (`makemigrations`, `migrate`).
* **QuerySets & Data Retrieval:**
  * Filtering data (e.g., `.filter()`, `.exclude()`)
  * Extracting specific values (`.values()`, `.first()`, `.last()`)
  * Ordering and chaining database queries.
* **Dynamic Rendering:** Injecting database QuerySets into HTML templates to display live table data.

### 5. Admin Panel & Data Management

* **Superuser:** Creating admin accounts (`createsuperuser`).
* **Model Registration:** Making models accessible and editable inside the Django Admin UI.
* **Admin Customization:** Enhancing the dashboard with List Displays, Search bars, and Sorting filters.

### 6. Advanced Features

* **File & Image Uploads:** Configuring `MEDIA_URL` and `MEDIA_ROOT` to safely handle user-uploaded files and display images.
* **Middleware:** Understanding how custom and built-in middleware processes requests before they hit the View, and responses before they reach the user.

### 7. APIs & Django REST Framework (DRF)

* **API Introduction:** Understanding the fundamentals of RESTful architecture.
* **Serialization:** Converting complex Django model instances into JSON format for modern frontend consumption (React, Mobile Apps).

---

## 🛠️ Practical Projects

* **Blog & Shop Modules:** Basic modular app routing and template rendering.
* **Complete TODO App:** A full CRUD (Create, Read, Update, Delete) application implementing databases, forms, and UI design.

---

## 💻 Tech Stack

* **Language:** Python 3.8+
* **Frameworks:** Django 5.x, Django REST Framework (DRF)
* **Frontend:** HTML5, CSS3, Bootstrap
* **Database:** SQLite (Development) / PostgreSQL (Production)
* **Tools:** VS Code, PIP, Virtualenv
