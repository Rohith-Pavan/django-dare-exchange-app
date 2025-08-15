#!/usr/bin/env python
"""
Build script for Netlify deployment
"""

import os
import sys
import subprocess
from pathlib import Path

# Set environment variables for Netlify
os.environ['NETLIFY'] = '1'
os.environ['DJANGO_SETTINGS_MODULE'] = 'dareproject.settings'

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed")
        print(f"Error: {e.stderr}")
        return False

def main():
    """Main build process"""
    print("Starting Netlify build process for Django Dare Exchange...")
    
    # Install dependencies
    if not run_command("pip install -r requirements.txt", "Installing dependencies"):
        sys.exit(1)
    
    # Setup Django
    import django
    django.setup()
    
    # Create database and run migrations
    if not run_command("python manage.py migrate --run-syncdb", "Setting up database"):
        print("Warning: Database setup failed, continuing...")
    
    # Create superuser (optional, for admin access)
    try:
        from django.contrib.auth.models import User
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            print("✓ Created admin user (username: admin, password: admin123)")
    except Exception as e:
        print(f"Warning: Could not create admin user: {e}")
    
    # Collect static files
    if not run_command("python manage.py collectstatic --noinput", "Collecting static files"):
        print("Warning: Static file collection failed, continuing...")
    
    print("\n✓ Build process completed!")
    print("\nDeployment ready for Netlify.")
    print("\nAccess your app at: https://your-site-name.netlify.app")
    print("Admin panel: https://your-site-name.netlify.app/.netlify/functions/django-app/admin/")

if __name__ == '__main__':
    main()