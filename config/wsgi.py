"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
from pathlib import Path

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

# Wrap with WhiteNoise for static files (Vercel compatible)
BASE_DIR = Path(__file__).resolve().parent.parent
staticfiles_dir = BASE_DIR / 'staticfiles'

if staticfiles_dir.exists():
    application = WhiteNoise(application, root=str(staticfiles_dir))
else:
    application = WhiteNoise(application)
