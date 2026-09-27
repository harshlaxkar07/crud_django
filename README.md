# Member Directory

A Django CRUD application for managing member records — create, read, update and delete, with model-level validation and feedback on every action.

---

## Highlights

| | |
|---|---|
| **Full CRUD** | Create, list, edit and delete members |
| **Model validation** | Names accept letters only, the email is checked for shape, all enforced at the model |
| **Feedback on every action** | Django's messages framework reports the result of each write |
| **Live filtering** | Filter the member table as you type, without a page reload |
| **Confirm before deleting** | Removals ask first |
| **Light and dark themes** | Toggled from the header and remembered between visits |

---

## Pages

**Home** — a landing page introducing the four operations, with direct routes into the table and the create form.

**Members** — headline counts and the full table: avatar, name, email, phone, age and record id, with inline edit and delete, plus a filter box that narrows the rows as you type.

**Add** — the model form laid out in a responsive grid, with field errors rendered inline.

**Edit** — the same form pre-filled from the record, with the member identified in the card header and a delete action alongside save.

---

## The model

```python
class Member(models.Model):
    firstname = models.CharField(
        max_length=50,
        validators=[RegexValidator(regex='^[a-zA-Z]*$', message='Only alphabets are allowed.')],
    )
    lastname = models.CharField(
        max_length=50,
        validators=[RegexValidator(regex='^[a-zA-Z]*$', message='Only alphabets are allowed.')],
    )
    age      = models.IntegerField()
    email    = models.EmailField(max_length=50)
    phone    = models.IntegerField()
    password = models.CharField(max_length=50)
```

Validation lives on the model, so it applies to the form, the admin and any other path that writes a member.

---

## Getting started

### Prerequisites

- Python 3.9 or newer

### 1. Install

```bash
git clone https://github.com/harshlaxkar07/crud_django.git
cd crud_django
python -m venv .venv && source .venv/bin/activate
pip install django
```

### 2. Set up the database

```bash
cd django_crud
python manage.py migrate
```

### 3. Run

```bash
python manage.py runserver
```

Open `http://localhost:8000`.

---

## Routes

| Path | Name | What it does |
|---|---|---|
| `/` | `home` | Landing page |
| `/read` | `read` | Every member in a filterable table |
| `/create` | `create` | Add a member |
| `/update/<member_id>/` | `update` | Edit a member |
| `/delete/<member_id>/` | `delete` | Remove a member |

---

## Project structure

```
crud_django/
└── django_crud/
    ├── manage.py
    ├── django_crud/
    │   ├── settings.py           Project settings
    │   └── urls.py               Root URL configuration
    └── crud/
        ├── models.py             Member, with its validators
        ├── views.py              home, read, create, update, delete
        ├── forms.py              MemberForm
        ├── urls.py               App routes
        ├── admin.py              Admin registration
        ├── migrations/
        ├── templates/
        │   ├── base.html         Shell, navigation, messages and theme toggle
        │   ├── home.html         Landing page
        │   ├── read.html         The member table
        │   ├── create.html       Add form
        │   └── update.html       Edit form
        └── static/css/style.css  Styling with light and dark themes
```
