# Lunex Presents — Digital Creative Agency

> A modern, production-ready website built with Django and Bootstrap 5 for **Lunex Presents**, a digital creative agency serving local businesses and brands.

---

## 🚀 Overview

- **Official Brand Name**: Lunex Presents
- **Email**: [lunex.presents@gmail.com](mailto:lunex.presents@gmail.com)
- **Instagram**: [@lunex.presents](https://instagram.com/lunex.presents)
- **Primary Services**:
  - Website Design & Development
  - Logo Design & Brand Identity
  - Posters & Social Media Creatives

---

## 🛠️ Technology Stack

- **Backend**: Python 3.12+ & Django 6.1
- **Frontend**: HTML5, CSS3, JavaScript (ES6+), Bootstrap 5.3
- **Icons**: Bootstrap Icons
- **Database**:
  - SQLite (Local development)
  - PostgreSQL (Production ready via `psycopg2-binary` & `DATABASE_URL`)
- **Static Assets**: WhiteNoise for high-performance static file serving
- **Image Processing**: Pillow
- **Admin**: Django Admin customized for managing services, portfolio projects, and customer enquiries

---

## 📂 Project Architecture

```
Lunex/
├── core/                       # Homepage, about section, FAQ, base views
├── services/                   # Services catalog, pricing/packages, details
├── portfolio/                  # Categorized portfolio projects, filterable grid, detail pages
├── contact/                    # Enquiry form, honeypot spam protection, admin triage
├── lunex_presents/             # Django project configuration
│   ├── settings/
│   │   ├── __init__.py         # Environment switcher (development vs production)
│   │   ├── base.py             # Shared settings
│   │   ├── development.py      # Local development configuration
│   │   └── production.py       # Production security headers, database, WhiteNoise
│   ├── urls.py                 # Root URL configuration + Sitemaps + Robots.txt
│   └── wsgi.py                 # Production WSGI application
├── static/                     # Brand CSS, JavaScript, and generated imagery
│   ├── css/style.css           # Premium dark aesthetic custom styles
│   ├── js/main.js              # Interactive animations, filter tabs, validation
│   └── images/                 # Favicon, OG share card, brand assets
├── templates/                  # Base layout, header, footer, 404, 500 error pages
├── seed_data.py                # Database seeder with concept projects & services
├── Procfile                    # Render/Heroku deployment command
├── requirements.txt            # Pinned production dependencies
└── .env.example                # Sample environment configuration
```

---

## 💻 Local Setup & Development

### 1. Clone & Enter the Repository
```bash
git clone <your-repo-url>
cd Lunex
```

### 2. Set Up a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
*(Development defaults work out-of-the-box with SQLite)*

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Seed Demo Data & Concept Projects
```bash
python seed_data.py
```

### 7. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 8. Run Development Server
```bash
python manage.py runserver 8000
```
Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 🔒 Security & Spam Prevention

- **CSRF Protection**: All forms utilize Django's built-in CSRF tokens.
- **Honeypot Field**: An invisible field (`website`) silently catches and drops automated bot spam submissions without breaking UX.
- **Security Headers**: HSTS, Content-Type-Options, X-Frame-Options, and SSL redirects configured for production.
- **WhiteNoise Cache**: Static assets are served with long-term cache headers and content hashes.

---

## ☁️ Deployment Guide (Render)

1. **Create a New Web Service** on [Render](https://render.com/).
2. Connect your GitHub repository.
3. Set the following build and start commands:
   - **Environment**: `Python 3`
   - **Build Command**:
     ```bash
     pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --no-input
     ```
   - **Start Command**:
     ```bash
     gunicorn lunex_presents.wsgi:application
     ```
4. **Environment Variables**:
   - `DJANGO_ENV`: `production`
   - `SECRET_KEY`: `<Generate a random secure 50+ character string>`
   - `ALLOWED_HOSTS`: `your-app-name.onrender.com`
   - `DATABASE_URL`: `postgres://...` *(Attach a Render PostgreSQL database)*
   - `DISABLE_COLLECTSTATIC`: `0`

---

## 📄 License & Credits

Built with pride for **Lunex Presents**. All rights reserved.
