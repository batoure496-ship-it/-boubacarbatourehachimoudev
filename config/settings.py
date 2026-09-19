


from pathlib import Path
import os


# ============================================================
# BASE DIRECTORY
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ============================================================
# SECURITY
# ============================================================

# En production, définir DJANGO_SECRET_KEY dans les variables
# d'environnement.
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "q)jnt714-4x^kxyj=2of5@*1b9i_nd1ef#(v#@^0n2esgggea$"
)

# Pour le déploiement, DEBUG doit être False.
DEBUG = os.environ.get("DJANGO_DEBUG", "False").lower() == "true"

# En local
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

# Ajouter les domaines personnalisés depuis les variables d'environnement
extra_hosts = os.environ.get("DJANGO_ALLOWED_HOSTS", "")

if extra_hosts:
    ALLOWED_HOSTS += [
        host.strip()
        for host in extra_hosts.split(",")
        if host.strip()
    ]

# Ajouter automatiquement le domaine fourni par Render
render_hostname = os.environ.get("RENDER_EXTERNAL_HOSTNAME")

if render_hostname:
    ALLOWED_HOSTS.append(render_hostname)
# ============================================================
# APPLICATIONS
# ============================================================

INSTALLED_APPS = [

    # Applications Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Applications du projet
    "projects",
    "services",
    "contacts",
    "blog",
]


# ============================================================
# MIDDLEWARE
# ============================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ============================================================
# URL CONFIGURATION
# ============================================================

ROOT_URLCONF = "config.urls"


# ============================================================
# TEMPLATES
# ============================================================

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
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
            ],
        },
    },
]


# ============================================================
# WSGI
# ============================================================

WSGI_APPLICATION = "config.wsgi.application"


# ============================================================
# DATABASE
# ============================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ============================================================
# PASSWORD VALIDATION
# ============================================================

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


# ============================================================
# INTERNATIONALIZATION
# ============================================================

LANGUAGE_CODE = "fr-fr"

TIME_ZONE = "Africa/Niamey"

USE_I18N = True

USE_TZ = True


# ============================================================
# STATIC FILES
# ============================================================

STATIC_URL = "/static/"

# Dossier utilisé par collectstatic
STATIC_ROOT = BASE_DIR / "staticfiles"

# Dossier contenant tes fichiers CSS, JS, images statiques
STATICFILES_DIRS = [
    BASE_DIR / "static",
]


# ============================================================
# MEDIA FILES
# ============================================================

# Fichiers envoyés par les utilisateurs
MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# ============================================================
# DEFAULT PRIMARY KEY
# ============================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ============================================================
# EMAIL
# ============================================================

# Pour le développement local :
# les emails sont affichés dans le terminal.
#
# Plus tard, pour la production, nous pourrons configurer
# Gmail SMTP ou un autre service d'envoi.

EMAIL_BACKEND = (
    "django.core.mail.backends.console.EmailBackend"
)

DEFAULT_FROM_EMAIL = "contact@hachimou.dev"


# ============================================================
# SECURITY — PRODUCTION
# ============================================================

# Ces options deviennent utiles lorsque le site sera en HTTPS.
#
# Elles ne gênent pas le fonctionnement local lorsque DEBUG=True.

if not DEBUG:

    SECURE_BROWSER_XSS_FILTER = True

    SECURE_CONTENT_TYPE_NOSNIFF = True

    X_FRAME_OPTIONS = "DENY"

    SECURE_HSTS_SECONDS = 31536000

    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

    SECURE_HSTS_PRELOAD = True

    SESSION_COOKIE_SECURE = True

    CSRF_COOKIE_SECURE = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

    SECURE_SSL_REDIRECT = True


# ============================================================
# CSRF — PRODUCTION
# ============================================================

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

