"""
Django local settings template for core project
"""

DEBUG = True

SECRET_KEY = "Zx[#c@L[Nk+HyxWqsIZ[d(I-}1g1aZXamuM5H#wl]LQYOOCm/=<jr'&aocPC"
FACEBOOK_APP_SECRET = "e0fc14f866941a1e4d15915440c5ee26"
DATABASES = {"default": {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": "core.db.sqlite3",
}}

ALLOWED_HOSTS = ["*"]
