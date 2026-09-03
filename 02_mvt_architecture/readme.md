### `02-MVT-Architecture-Explained/README.md`

```markdown
# MVT Architecture Explained

This section explains the core design pattern Django uses to process requests and serve webpages.

The goal of this topic is to understand **how Django organizes code and how the Model, View, and Template work together.**

---

## What is MVT?

**MVT stands for Model, View, and Template.** 

It is the backbone of any Django project. When a user requests a page, these three components communicate to figure out what data to get, how to process it, and how to display it.

---

## The Three Components

### 1. Model (Database)
The Model is responsible for your data. It talks directly to your database (like SQLite or PostgreSQL) to save, update, or fetch information.

### 2. View (Business Logic)
The View is the brain. It acts as a middleman between the Model and the Template. It receives the user's request, asks the Model for data, processes that data, and passes it to the Template.

### 3. Template (Presentation)
The Template is what the user actually sees. It is made of HTML combined with Django Template Language (DTL). It takes the raw data from the View and makes it look visually appealing.

---

## The Workflow (How it Works)

Here is the step-by-step flow when someone visits a Django website:

```text
1. User enters URL in Browser
   ↓
2. URL Dispatcher (urls.py) checks where to send the request
   ↓
3. View is triggered
   ↓
4. View asks Model for data (if needed)
   ↓
5. Model fetches data from Database and gives it to View
   ↓
6. View passes data to the Template
   ↓
7. Template renders the final HTML and sends it to the User


MVC Pattern          MVT Pattern (Django)
-----------          --------------------
Model          =     Model
Controller     =     View
View           =     Template
