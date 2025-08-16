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

# Load initial data fixtures
echo "Loading initial sample data..."
python manage.py loaddata initial_data.json

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build completed successfully!"