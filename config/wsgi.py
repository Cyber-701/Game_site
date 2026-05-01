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

# Wrap with WhiteNoise for static files
# Handle both local and Vercel paths
BASE_DIR = Path(__file__).resolve().parent.parent
static_root = BASE_DIR / 'staticfiles'

if static_root.exists():
    application = WhiteNoise(application, root=str(static_root))
else:
    # Fallback for Vercel serverless
    vercel_static = Path('/var/task/staticfiles')
    if vercel_static.exists():
        application = WhiteNoise(application, root=str(vercel_static))
