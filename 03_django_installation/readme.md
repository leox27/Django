# Chapter 03 - Django Installation and Virtual Environment Setup

## 1. Python for Django

Django is a **Python web framework**, so Python must be installed on your system before you can create and run a Django project.

### Check if Python is Installed

**Windows:**

```bash
python --version
```

**macOS/Linux:**

```bash
python3 --version
```

If Python is installed, the command will display its version.

Example:

```text
Python 3.13.5
```

The Python version should be compatible with the Django version you are using.

---

## 2. Installing Python

If Python is not installed on your system, download it from the official Python website.

During installation on Windows, make sure to check:

**Add Python to PATH**

This allows you to use Python commands directly from the terminal.

After installation, verify it:

```bash
python --version
```

On macOS/Linux:

```bash
python3 --version
```

---

## 3. What is PIP?

**PIP** is Python's package installer.

It is used to install external Python packages and libraries.

For example, Django is installed using PIP.

Other packages such as Flask, NumPy, Pandas, and many other Python libraries can also be installed using PIP.

### Check PIP Version

**Windows:**

```bash
pip --version
```

**macOS/Linux:**

```bash
pip3 --version
```

PIP normally comes with modern Python installations, so it usually does not need to be installed separately.

---

## 4. Installing Django

Once Python and PIP are available, Django can be installed using PIP.

**Windows:**

```bash
pip install django
```

**macOS/Linux:**

```bash
pip3 install django
```

PIP downloads Django and installs it along with its required dependencies.

> **Important:** It is recommended to install Django inside a virtual environment instead of installing it directly into the global Python environment.

---

## 5. Checking the Django Version

After installing Django, check the installed version:

```bash
django-admin --version
```

Example:

```text
5.2.4
```

The exact version may be different depending on when Django is installed.

Checking the version is useful because different Django versions may have differences in features, commands, and APIs.

---

## 6. Installing VS Code

**Visual Studio Code (VS Code)** is a code editor used to write and manage Django projects.

A Django project contains multiple Python files, HTML templates, configuration files, and other resources.

After installing VS Code:

1. Create a folder for your Django project.
2. Open that folder in VS Code.
3. Open the integrated terminal.
4. Run Python and Django commands from the terminal.

The integrated terminal can be opened from:

**Terminal → New Terminal**

This allows you to work with project files and run commands from the same application.

---

## 7. What is a Virtual Environment?

A **Virtual Environment** is an isolated Python environment created for a project.

It allows a project to have its own Python packages and package versions without affecting other projects.

### Why Do We Need a Virtual Environment?

Imagine you are working on multiple Django projects.

For example:

- Project A requires one version of Django.
- Project B requires another version of Django.

If everything is installed globally, different projects can end up depending on conflicting package versions.

This can cause compatibility problems.

A virtual environment solves this problem by keeping each project's dependencies separate.

### Without a Virtual Environment

```text
Computer
│
├── Project A
│   └── Django Version A
│
└── Project B
    └── Django Version B
```

Both projects use the same global Python environment.

### With Virtual Environments

```text
Computer
│
├── Project A
│   └── Virtual Environment
│       └── Django Version A
│
└── Project B
    └── Virtual Environment
        └── Django Version B
```

Each project gets its own isolated environment.

> **Main idea:** A virtual environment prevents dependencies of one project from interfering with another project.

---

## 8. Is a Virtual Environment Mandatory?

Technically, a virtual environment is **optional**.

However, it is a **recommended practice**, especially when working on multiple or professional projects.

If different projects require different versions of Django or other packages, virtual environments make it easier to manage those dependencies.

---

## 9. Installing `virtualenv`

The `virtualenv` package can be used to create virtual environments.

Install it using PIP.

**Windows:**

```bash
pip install virtualenv
```

**macOS/Linux:**

```bash
pip3 install virtualenv
```

---

## 10. Creating a Virtual Environment

First, open your project folder in the terminal.

Then run:

```bash
virtualenv myenv
```

This creates a folder named `myenv`.

Here:

- `virtualenv` → The tool used to create the virtual environment.
- `myenv` → The name of the virtual environment.
- You can use another name such as `venv`.

For example:

```bash
virtualenv venv
```

The resulting structure may look like:

```text
DjangoProject/
└── myenv/
```

---

## 11. Python's Built-in `venv`

Python also provides a built-in module called `venv` for creating virtual environments.

You can create a virtual environment without installing the separate `virtualenv` package:

```bash
python -m venv venv
```

On systems where Python 3 is used as `python3`:

```bash
python3 -m venv venv
```

The course demonstrates `virtualenv`, but Python's built-in `venv` is also a standard way to create a virtual environment.

---

## 12. Activating the Virtual Environment

Creating a virtual environment does not automatically activate it.

You need to activate the environment before working inside it.

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

---

## 13. How to Know the Virtual Environment is Active

After successfully activating the environment, its name appears at the beginning of the terminal prompt.

For example:

```text
(myenv) C:\Users\YourName\DjangoProject>
```

The `(myenv)` indicates that the virtual environment is active.

Once the environment is active, packages installed using PIP will be installed inside that environment.

For example:

```bash
pip install django
```

This installs Django inside the active virtual environment.

---

## 14. Virtual Environment with VS Code

VS Code makes working with virtual environments easier.

A common workflow is:

```text
Create Project Folder
        ↓
Open Folder in VS Code
        ↓
Open VS Code Terminal
        ↓
Create Virtual Environment
        ↓
Activate Virtual Environment
        ↓
Install Django
        ↓
Create Django Project
```

The integrated terminal allows you to run commands while working directly inside your project folder.

---

## 15. Do Not Upload the Virtual Environment to GitHub

A virtual environment contains many files and installed packages specific to your local system.

Therefore, you should **not upload the entire virtual environment to GitHub**.

For example:

```text
venv/
```

or:

```text
myenv/
```

Add the virtual environment folder to `.gitignore` instead.

Example:

```gitignore
venv/
myenv/
```

This prevents Git from tracking the virtual environment.

Project dependencies can later be stored in a `requirements.txt` file so that the environment can be recreated on another system.

---

## 16. Important Commands

### Check Python

```bash
python --version
```

### Check Python 3

```bash
python3 --version
```

### Check PIP

```bash
pip --version
```

### Check PIP 3

```bash
pip3 --version
```

### Install Django

```bash
pip install django
```

### Check Django Version

```bash
django-admin --version
```

### Install `virtualenv`

```bash
pip install virtualenv
```

### Create Virtual Environment

```bash
virtualenv myenv
```

### Create Environment Using Python `venv`

```bash
python -m venv venv
```

### Activate on Windows

```bash
venv\Scripts\activate
```

### Activate on macOS/Linux

```bash
source venv/bin/activate
```

---

## 17. Common Mistakes

### Python Command Is Not Recognized

Python may not be installed correctly or its PATH may not be configured.

On Windows, make sure **Add Python to PATH** was selected during installation.

### Installing Django Globally

Installing Django globally can create dependency conflicts when working on multiple projects.

It is better to activate a virtual environment first and then install Django.

### Creating but Not Activating the Virtual Environment

Creating the environment is not enough.

You must activate it before installing and using project-specific packages.

### Uploading `venv` to GitHub

Do not upload the entire virtual environment.

Add it to `.gitignore` instead.

---

## 18. Complete Setup Flow

The complete setup process can be remembered as:

```text
Install Python
      ↓
Check Python
      ↓
Check PIP
      ↓
Install VS Code
      ↓
Create Project Folder
      ↓
Create Virtual Environment
      ↓
Activate Virtual Environment
      ↓
Install Django
      ↓
Check Django Version
      ↓
Start Django Project
```

---

## 19. Quick Revision

| Tool | Purpose |
|------|---------|
| Python | Required because Django is a Python framework |
| PIP | Used to install Python packages |
| Django | Python web framework |
| VS Code | Code editor |
| Virtual Environment | Keeps project dependencies isolated |

### Remember

**Python → PIP → Virtual Environment → Django**

A typical Django setup involves:

1. Installing Python.
2. Checking PIP.
3. Installing or creating a virtual environment.
4. Activating the virtual environment.
5. Installing Django.
6. Checking the Django version.
7. Starting the Django project.

---

## 20. Key Takeaways

- Django is a **Python web framework**.
- Python must be installed before using Django.
- PIP is used to install Python packages.
- Django can be installed using PIP.
- `django-admin --version` checks the installed Django version.
- VS Code can be used to write and manage Django projects.
- A virtual environment provides an isolated environment for a project.
- Virtual environments help prevent dependency and version conflicts.
- The virtual environment must be activated before using it.
- The environment name appears in the terminal when it is active.
- Virtual environments should not be committed to GitHub.
- `requirements.txt` can be used to store project dependencies.

---

## What's Next?

The development environment is now ready.

In the next chapter, we will **create and run our first Django project**.