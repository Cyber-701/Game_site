#!/bin/bash
# Build script for Vercel deployment

echo "Building Django project for Vercel..."

# Collect static files
python manage.py collectstatic --noinput

# Copy static files to public directory for Vercel static hosting
mkdir -p public/static
cp -r staticfiles/* public/static/

echo "Build complete!"
