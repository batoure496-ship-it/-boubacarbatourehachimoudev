from pathlib import Path
import os

import dj_database_url


# =========================================================
# BASE DIRECTORY
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# =========================================================
# SECURITY
# =========================================================

DEBUG = os.environ.get("DJANGO_DEBUG", "False").lower() == "true"

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
if not SECRET_KEY:
    if not DEBUG:
        raise RuntimeError("DJANGO_SECRET_KEY must be set when DEBUG is false.")
    SECRET_KEY = "dev-only-insecure-key-do-not-use-in-production"


# =========================================================
# ALLOWED HOSTS
# =========================================================

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

extra_hosts = os.environ.get("DJANGO_ALLOWED_HOSTS", "")

if extra_hosts:
    ALLOWED_HOSTS += [
        host.strip()
        for host in extra_hosts.split(",")
        if host.strip()
    ]

render_hostname = os.environ.get("RENDER_EXTERNAL_HOSTNAME")

if render_hostname:
    ALLOWED_HOSTS.append(render_hostname)


# =========================================================
# APPLICATIONS
# =========================================================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Application existante du projet
    "contacts",

    # Packages installés
    "rest_framework",
    "django_filters",
    "corsheaders",
]


# =========================================================
# MIDDLEWARE
# =========================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # WhiteNoise : fichiers CSS / JS / images statiques
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =========================================================
# URL CONFIGURATION
# =========================================================

ROOT_URLCONF = "config.urls"


# =========================================================
# TEMPLATES
# =========================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "templates",
        ],

        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# =========================================================
# WSGI
# =========================================================

WSGI_APPLICATION = "config.wsgi.application"


# =========================================================
# DATABASE
# =========================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

if database_url := os.environ.get("DATABASE_URL"):
    DATABASES["default"] = dj_database_url.parse(
        database_url,
        conn_max_age=600,
        conn_health_checks=True,
    )


# =========================================================
# PASSWORD VALIDATION
# =========================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# =========================================================
# INTERNATIONALIZATION
# =========================================================

LANGUAGE_CODE = "fr-fr"

TIME_ZONE = "Africa/Niamey"

USE_I18N = True

USE_TZ = True


# =========================================================
# STATIC FILES
# =========================================================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]


# =========================================================
# WHITE NOISE
# =========================================================

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },

    "staticfiles": {
        "BACKEND": (
            "whitenoise.storage."
            "CompressedManifestStaticFilesStorage"
        ),
    },
}


# =========================================================
# MEDIA FILES
# =========================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# =========================================================
# DEFAULT PRIMARY KEY
# =========================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# =========================================================
# DJANGO REST FRAMEWORK
# =========================================================

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
}


# =========================================================
# CORS
# =========================================================

CORS_ALLOWED_ORIGINS = []

extra_cors_origins = os.environ.get(
    "DJANGO_CORS_ALLOWED_ORIGINS",
    ""
)

if extra_cors_origins:
    CORS_ALLOWED_ORIGINS = [
        origin.strip()
        for origin in extra_cors_origins.split(",")
        if origin.strip()
    ]


# =========================================================
# CSRF
# =========================================================

CSRF_TRUSTED_ORIGINS = []

extra_csrf_origins = os.environ.get(
    "DJANGO_CSRF_TRUSTED_ORIGINS",
    ""
)

if extra_csrf_origins:
    CSRF_TRUSTED_ORIGINS = [
        origin.strip()
        for origin in extra_csrf_origins.split(",")
        if origin.strip()
    ]


# =========================================================
# PRODUCTION SECURITY
# =========================================================

if not DEBUG:

    SECURE_BROWSER_XSS_FILTER = True

    SECURE_CONTENT_TYPE_NOSNIFF = True

    X_FRAME_OPTIONS = "DENY"

    SECURE_HSTS_SECONDS = 31536000

    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

    SECURE_HSTS_PRELOAD = True

    SESSION_COOKIE_SECURE = True

    CSRF_COOKIE_SECURE = True

    SECURE_PROXY_SSL_HEADER = (
        "HTTP_X_FORWARDED_PROTO",
        "https"
    )

    # HTTPS obligatoire uniquement sur Render
    if os.environ.get("RENDER"):
        SECURE_SSL_REDIRECT = True
    else:
        SECURE_SSL_REDIRECT = False
# =========================================================
# SESSION SECURITY
# =========================================================

SESSION_COOKIE_HTTPONLY = True

SESSION_COOKIE_SAMESITE = "Lax"

CSRF_COOKIE_SAMESITE = "Lax"


# =========================================================
# EMAIL
# =========================================================

EMAIL_BACKEND = os.environ.get(
    "DJANGO_EMAIL_BACKEND",
    "django.core.mail.backends.console.EmailBackend",
)

DEFAULT_FROM_EMAIL = os.environ.get(
    "DJANGO_DEFAULT_FROM_EMAIL",
    "webmaster@localhost",
)


# =========================================================
# LOGIN / LOGOUT
# =========================================================

LOGIN_URL = "/admin/login/"

LOGIN_REDIRECT_URL = "/"

LOGOUT_REDIRECT_URL = "/"


# =========================================================
# UPLOADS
# =========================================================

DATA_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024

FILE_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024
