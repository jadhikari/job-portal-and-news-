
```markdown
# News & Job Portal, User Management and Core App

This Django project serves as a core application for managing news, job postings, blogs, and videos with integrated user management. It leverages **django-ckeditor** for rich text editing in all header and content fields and automatically assigns the logged-in user when creating new records.

## Features

- **Unique ID:**  
  Each record automatically gets a non‑editable, unique 6‑character alphanumeric ID.
  
- **Rich Text Editing:**  
  All header and content fields use `RichTextField` from django‑ckeditor, allowing users to format text (change fonts, add bullets, adjust line spacing, etc.).
  
- **User Association:**  
  The admin auto-assigns the currently logged-in user to each new record.

- **Models Included:**  
  - **News:** Includes optional image, headers, and content in three languages (JA, ENG, NEP).  
  - **Blog:** Contains an optional image and headers.  
  - **Video:** Contains headers and a URL link.  
  - **Job:** Contains headers and content fields.

## Setup

1. **Install Dependencies:**

   ```bash
   pip install django django-ckeditor
   ```

2. **Update `INSTALLED_APPS` in `settings.py`:**

   ```python
   INSTALLED_APPS = [
       # ... other apps ...
       'ckeditor',
       'core',  # your main app
   ]
   ```

3. **Configure CKEditor in `settings.py`:**

   ```python
   CKEDITOR_CONFIGS = {
       'default': {
           'toolbar': 'full',
           'height': 300,
           'width': '100%',
       },
   }
   ```

4. **Run Migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the Server:**

   ```bash
   python manage.py runserver
   ```



1. **To compile translation file:**

   ```bash
   django-admin compilemessages 
   ```

```
