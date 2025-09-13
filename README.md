# Resto – Django Restaurant Website

A full-featured restaurant website built with Django. Easily manage your menu, reservations, and customer messages through a secure admin panel.

---

## Features

- **Dynamic Menu:** Add, edit, and display menu items by category with images.
- **Reservation System:** Customers can book tables; admins manage reservations.
- **Contact Form:** Visitors send messages; admins view all submissions.
- **Admin Panel:** Manage all content securely.
- **Responsive Design:** Works on desktop and mobile.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Adarshow/Resto-App2.git
cd Resto-App2
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
pip install Pillow
```

### 3. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create a Superuser

```bash
python manage.py createsuperuser
```

### 5. Run the Server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) for the site and [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) for the admin panel.

---

## Usage

- **Add Categories & Menu Items:** Use the admin panel to create categories and menu items. Upload images for each item.
- **Manage Reservations & Messages:** View and manage all reservations and contact messages in the admin panel.
- **Customize Content:** Edit templates and static files for your branding.

---

## Project Structure

```
restaurant_site/      # Django project settings
menu/                 # Main app (models, views, templates)
manage.py             # Django management script
requirements.txt      # Python dependencies
Procfile, render.yaml # Deployment configs
```

---

## Deployment

Ready for deployment on Render, Heroku, or any cloud platform.  
See `render.yaml` for Render deployment instructions.

---

## License

MIT License

---

## Credits

Developed by Adarshow  
Powered by Django & Bootstrap
