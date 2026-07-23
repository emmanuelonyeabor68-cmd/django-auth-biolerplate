# Django Auth Boilerplate

A production-ready authentication backend built with Django, Djoser, SimpleJWT, and Google OAuth. Features email verification, JWT authentication with httpOnly cookies, password reset, token blacklisting, and Google OAuth login. Built as a reusable foundation for any web application requiring robust authentication.

## Live URLs

Backend: https://django-auth-biolerplate.onrender.com 

## Tech Stack

- Django 6.0, Django REST Framework, Djoser, SimpleJWT
- Social Auth App Django for Google OAuth
- PostgreSQL on Neon
- Resend for email delivery
- Deployed on Render

## Features

- Custom user model with email authentication
- Registration with email verification — accounts inactive until activated
- Google OAuth login — users activated automatically via Google verified email
- JWT access tokens (15 min) and refresh tokens (7 days)
- Refresh token in httpOnly cookie — inaccessible to JavaScript
- Silent token refresh via Axios interceptor
- Session restore on page refresh
- Forgot password and reset password via email
- Token blacklisting on logout
- CORS and CSRF configured for production

## Authentication Flows

Email/Password: Register → activation email sent → user clicks link → account activated → login → access token in memory + refresh token in httpOnly cookie → token expires → silent refresh → logout → token blacklisted + cookie cleared

Google OAuth: Click Login with Google → redirected to Google → user authenticates → Django pipeline runs → user created and activated → JWT issued → refresh token set as httpOnly cookie → redirected to dashboard

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
| GET | /social-auth/login/google-oauth2/ | Initiate Google OAuth |

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
DATABASE_URL=sqlite:///db.sqlite3
CORS_ALLOWED_ORIGINS=http://127.0.0.1:3000
CSRF_TRUSTED_ORIGINS=http://127.0.0.1:3000,http://127.0.0.1:8000
FRONTEND_URL=127.0.0.1:3000
SITE_NAME=Auth App
RESEND_API_KEY=your-resend-api-key
DEFAULT_FROM_EMAIL=onboarding@resend.dev
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret

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
| ENVIRONMENT | production |
| COOKIE_SECURE | True |
| RESEND_API_KEY | Your Resend key |
| DEFAULT_FROM_EMAIL | noreply@yourdomain.com |
| GOOGLE_CLIENT_ID | Your Google OAuth client ID |
| GOOGLE_CLIENT_SECRET | Your Google OAuth client secret |

## Google OAuth Setup

1. Go to console.cloud.google.com
2. Create a project and enable Google OAuth API
3. Create OAuth 2.0 credentials
4. Add authorized redirect URI: https://your-app.onrender.com/social-auth/complete/google-oauth2/
5. Add your Client ID and Secret to environment variables

## Security

- httpOnly cookie protects refresh token from XSS
- Short-lived access tokens minimize exposure
- Server-side token blacklisting on logout
- Passwords hashed with PBKDF2
- Google OAuth users verified automatically via Google
- DEBUG=False in production
- Secret key in environment variable

## Frontend Repository

https://github.com/emmanuelonyeabor68-cmd/react_auth_frontend
