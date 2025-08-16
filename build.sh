#!/bin/bash

# Build script for Render deployment
echo "Starting Django build process..."

# Set environment variables for production
export DEBUG=False
export ALLOWED_HOSTS="*"

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run Django system check
echo "Running Django system check..."
python manage.py check --deploy

# Run migrations
echo "Running database migrations..."
python manage.py migrate

# Populate database with sample data (Force run)
echo "Populating database with sample data..."
python manage.py populate_render_db --verbosity=2

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build completed successfully!"