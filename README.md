# Django Auth Boilerplate

A production-ready authentication backend built with Django, Djoser, and SimpleJWT. Features email verification, JWT authentication with httpOnly cookies, password reset, and token blacklisting. Built as a reusable foundation for any web application requiring robust authentication.

## Live URLs

Backend: https://django-auth-biolerplate.onrender.com 

## Tech Stack

- Django 6.0, Django REST Framework, Djoser, SimpleJWT
- PostgreSQL on Neon
- Resend for email delivery
- Deployed on Render

## Features

- Custom user model with email authentication
- Registration with email verification — accounts inactive until activated
- JWT access tokens (15 min) and refresh tokens (7 days)
- Refresh token in httpOnly cookie — inaccessible to JavaScript
- Silent token refresh via Axios interceptor
- Session restore on page refresh
- Forgot password and reset password via email
- Token blacklisting on logout
- CORS and CSRF configured for production

## Authentication Flow

Register → activation email sent → user clicks link → account activated → login → access token in memory + refresh token in httpOnly cookie → token expires → silent refresh → logout → token blacklisted + cookie cleared

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/auth/users/ | Register |
| POST | /api/auth/users/activation/ | Activate account |
| POST | /api/auth/login/ | Login |
| POST | /api/auth/refresh/ | Refresh access token |
| POST | /api/auth/logout/ | Logout |
| GET | /api/auth/users/me/ | Get current user |
| POST | /api/auth/users/reset_password/ | Forgot password |
| POST | /api/auth/users/reset_password_confirm/ | Reset password |

## Local Setup

git clone https://github.com/emmanuelonyeabor68-cmd/django-auth-biolerplate.git
cd django-auth-biolerplate/auth
python -m venv venv
venv\Scripts\activate
pip install -r requirement.txt

Create .env file:

SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
CORS_ALLOWED_ORIGINS=http://127.0.0.1:3000
CSRF_TRUSTED_ORIGINS=http://127.0.0.1:3000,http://127.0.0.1:8000
FRONTEND_URL=127.0.0.1:3000
SITE_NAME=Auth App
COOKIE_SECURE=False
RESEND_API_KEY=your-resend-api-key
DEFAULT_FROM_EMAIL=onboarding@resend.dev

Run:

python manage.py migrate
python manage.py runserver

## Render Deployment

Build command: pip install -r requirement.txt && python manage.py migrate && python manage.py update_site

Start command: gunicorn auth.wsgi

| Key | Value |
|-----|-------|
| SECRET_KEY | Generated secret key |
| DEBUG | False |
| ALLOWED_HOSTS | your-app.onrender.com |
| DATABASE_URL | Neon PostgreSQL URL |
| CORS_ALLOWED_ORIGINS | https://your-frontend.vercel.app |
| CSRF_TRUSTED_ORIGINS | https://your-frontend.vercel.app,https://your-app.onrender.com |
| FRONTEND_URL | your-frontend.vercel.app |
| COOKIE_SECURE | True |
| RESEND_API_KEY | Your Resend key |
| DEFAULT_FROM_EMAIL | noreply@yourdomain.com |

## Security

- httpOnly cookie protects refresh token from XSS
- Short-lived access tokens minimize exposure
- Server-side token blacklisting on logout
- Passwords hashed with PBKDF2
- DEBUG=False in production
- Secret key in environment variable
