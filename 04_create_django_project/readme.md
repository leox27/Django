# Chapter 04 - Creating and Running the First Django Project

In this chapter, we will create our **first Django project**, understand the basic project structure, and run the Django development server.

---

## 1. Check Django Installation

Before creating a Django project, first make sure Django is installed on your system.

Run:

```bash
django-admin --version
```

If Django is installed, this command will show the installed Django version.

Example:

```text
5.2.4
```

If Django is not installed, install it using PIP:

```bash
pip install django
```

On systems where `pip3` is used:

```bash
pip3 install django
```

Once Django is installed and its version is displayed, you are ready to create a project.

---

## 2. Create a Django Project

Django provides the `startproject` command to create a new Django project.

The basic syntax is:

```bash
django-admin startproject project_name
```

For example:

```bash
django-admin startproject myproject
```

Here:

- `django-admin` → Django's command-line utility.
- `startproject` → Command used to create a new Django project.
- `myproject` → Name of the project.

After running the command, Django creates a new folder containing the initial project files.

---

## 3. Basic Django Project Structure

After creating the project, the structure looks similar to this:

```text
myproject/
│
├── manage.py
│
└── myproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

There are two `myproject` levels here:

- The **outer `myproject` folder** is the project directory.
- The **inner `myproject` folder** is the Python package containing the project's configuration files.

---

## 4. `manage.py`

`manage.py` is one of the most important files in a Django project.

It is used to run Django management commands.

For example, it can be used to:

- Start the development server.
- Create Django applications.
- Run database migrations.
- Perform other Django management tasks.

Examples:

```bash
python manage.py runserver
```

```bash
python manage.py startapp app_name
```

```bash
python manage.py migrate
```

The exact commands will be covered in detail in later chapters.

---

## 5. `__init__.py`

The `__init__.py` file indicates that the directory can be treated as a Python package.

The file is normally empty in a newly created Django project.

You generally do not need to add anything to it when starting a Django project.

---

## 6. `settings.py`

The `settings.py` file contains the main **configuration and settings** of the Django project.

It controls different aspects of the project, such as:

- Installed applications.
- Database configuration.
- Middleware.
- Templates.
- Static files.
- Security-related settings.
- Other Django configurations.

We will study `settings.py` in detail in later chapters.

---

## 7. `urls.py`

The `urls.py` file is used for **URL mapping**.

It determines which URL patterns should be connected to which views.

For example, a URL such as:

```text
/about/
```

can later be connected to a particular Django view.

The detailed working of URL routing will be covered in later chapters.

---

## 8. `asgi.py`

`asgi.py` is related to **ASGI (Asynchronous Server Gateway Interface)**.

It provides an entry point for deploying the Django project with ASGI-compatible servers.

ASGI is useful for applications that need asynchronous capabilities.

The detailed purpose and deployment process will be covered later.

---

## 9. `wsgi.py`

`wsgi.py` is related to **WSGI (Web Server Gateway Interface)**.

It provides an entry point for deploying a Django project with WSGI-compatible web servers.

It is commonly used when deploying traditional synchronous Django applications.

The detailed deployment process will be covered later.

---

## 10. Navigate Inside the Project

After creating the project, move into the project directory using the `cd` command.

For example:

```bash
cd myproject
```

Now the terminal is inside the directory containing `manage.py`.

This is important because Django management commands are normally run from the directory containing `manage.py`.

---

## 11. Run the Django Development Server

To start the Django development server, use:

**Windows:**

```bash
python manage.py runserver
```

**macOS/Linux:**

```bash
python3 manage.py runserver
```

The `runserver` command starts Django's built-in development server.

---

## 12. Understanding the `runserver` Command

The command:

```bash
python manage.py runserver
```

can be understood as:

- `python` → Runs the Python interpreter.
- `manage.py` → Django project's command-line utility.
- `runserver` → Starts Django's development server.

On macOS/Linux, you may use:

```bash
python3 manage.py runserver
```

---

## 13. Django Development Server

After running the server, Django displays a message indicating that the development server is running.

A typical address is:

```text
http://127.0.0.1:8000/
```

You can copy this address and open it in your browser.

The exact port can be different if you specify another port when starting the server.

---

## 14. Django Welcome Page

If everything is configured correctly, opening the development server address in your browser will display Django's default welcome page.

The page confirms that:

- Django is installed correctly.
- The project was created successfully.
- The development server is running.
- Your Django application is ready for further development.

---

## 15. Stop the Development Server

To stop the Django development server, press:

```text
CTRL + C
```

This stops the development server running in the terminal.

---

## 16. Changing the Development Server Port

By default, Django uses port `8000`.

You can start the development server on another port by specifying the port number.

For example:

```bash
python manage.py runserver 8080
```

The server will then be available at:

```text
http://127.0.0.1:8080/
```

Port configuration and other server options will be explored later.

---

## 17. Complete Process

The complete process for creating and running the first Django project is:

```text
Check Django Installation
        ↓
Create Django Project
        ↓
Open Project Directory
        ↓
Understand Basic Project Structure
        ↓
Run Development Server
        ↓
Open Server Address in Browser
        ↓
Django Welcome Page
```

---

## 18. Important Commands

### Check Django Version

```bash
django-admin --version
```

### Install Django

```bash
pip install django
```

### Create a Django Project

```bash
django-admin startproject myproject
```

### Enter the Project Directory

```bash
cd myproject
```

### Start the Development Server on Windows

```bash
python manage.py runserver
```

### Start the Development Server on macOS/Linux

```bash
python3 manage.py runserver
```

### Start the Server on a Specific Port

```bash
python manage.py runserver 8080
```

### Stop the Server

```text
CTRL + C
```

---

## 19. Quick Revision

| File | Purpose |
|------|---------|
| `manage.py` | Runs Django management commands |
| `__init__.py` | Makes the directory a Python package |
| `settings.py` | Contains project configuration and settings |
| `urls.py` | Handles URL mapping |
| `asgi.py` | ASGI deployment entry point |
| `wsgi.py` | WSGI deployment entry point |

---

## 20. Key Takeaways

- `django-admin --version` can be used to check whether Django is installed.
- `django-admin startproject` creates a new Django project.
- `manage.py` is used to execute Django management commands.
- `settings.py` contains the project's configuration.
- `urls.py` is used for URL mapping.
- `asgi.py` provides an ASGI entry point.
- `wsgi.py` provides a WSGI entry point.
- The development server can be started using `runserver`.
- The default development server normally runs on port `8000`.
- The server can be stopped using `CTRL + C`.
- The development server allows us to test the Django project locally.

---

## What's Next?

The first Django project has been created and successfully run.

In the next chapter, we will understand the **Django project folder structure in detail** and learn the purpose of each file.