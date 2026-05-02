#!/bin/bash
# Build script for Vercel deployment

echo "Building Django project for Vercel..."

# Collect static files (Whitenoise will serve them)
python manage.py collectstatic --noinput

echo "Build complete!"
