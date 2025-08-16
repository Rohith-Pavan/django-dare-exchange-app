#!/usr/bin/env python3
"""
PythonAnywhere Deployment Script for Django Dare Exchange

This script automates the deployment process for PythonAnywhere.
Run this script in your PythonAnywhere Bash console after uploading your project.

Usage:
    python3 deploy_pythonanywhere.py
"""

import os
import sys
import subprocess
import getpass

def run_command(command, description=""):
    """Run a shell command and handle errors."""
    print(f"\n{'='*50}")
    if description:
        print(f"📋 {description}")
    print(f"🔧 Running: {command}")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        if e.stdout:
            print(f"Output: {e.stdout}")
        if e.stderr:
            print(f"Error: {e.stderr}")
        return False

def get_username():
    """Get PythonAnywhere username from current path or user input."""
    current_path = os.getcwd()
    if '/home/' in current_path:
        username = current_path.split('/home/')[1].split('/')[0]
        print(f"🔍 Detected username: {username}")
        confirm = input(f"Is '{username}' your PythonAnywhere username? (y/n): ").lower()
        if confirm == 'y':
            return username
    
    return input("Enter your PythonAnywhere username: ")

def update_config_files(username):
    """Update configuration files with the actual username."""
    print(f"\n📝 Updating configuration files for user: {username}")
    
    # Update pythonanywhere_settings.py
    settings_file = 'pythonanywhere_settings.py'
    if os.path.exists(settings_file):
        with open(settings_file, 'r') as f:
            content = f.read()
        
        content = content.replace('yourusername', username)
        
        with open(settings_file, 'w') as f:
            f.write(content)
        print(f"✅ Updated {settings_file}")
    
    # Update pythonanywhere_wsgi.py
    wsgi_file = 'pythonanywhere_wsgi.py'
    if os.path.exists(wsgi_file):
        with open(wsgi_file, 'r') as f:
            content = f.read()
        
        content = content.replace('yourusername', username)
        
        with open(wsgi_file, 'w') as f:
            f.write(content)
        print(f"✅ Updated {wsgi_file}")

def main():
    print("🚀 Django Dare Exchange - PythonAnywhere Deployment Script")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("❌ Error: manage.py not found. Please run this script from your Django project directory.")
        sys.exit(1)
    
    # Get username
    username = get_username()
    
    # Update configuration files
    update_config_files(username)
    
    # Create virtual environment
    if not os.path.exists('venv'):
        if not run_command("python3.11 -m venv venv", "Creating virtual environment"):
            print("❌ Failed to create virtual environment")
            return False
    else:
        print("✅ Virtual environment already exists")
    
    # Activate virtual environment and install dependencies
    activate_cmd = "source venv/bin/activate"
    
    if not run_command(f"{activate_cmd} && pip install --upgrade pip", "Upgrading pip"):
        print("⚠️  Warning: Failed to upgrade pip, continuing...")
    
    if not run_command(f"{activate_cmd} && pip install -r pythonanywhere_requirements.txt", "Installing dependencies"):
        print("❌ Failed to install dependencies")
        return False
    
    # Run migrations
    settings_module = "dareproject.pythonanywhere_settings"
    if not run_command(f"{activate_cmd} && python manage.py migrate --settings={settings_module}", "Running database migrations"):
        print("❌ Failed to run migrations")
        return False
    
    # Collect static files
    if not run_command(f"{activate_cmd} && python manage.py collectstatic --settings={settings_module} --noinput", "Collecting static files"):
        print("❌ Failed to collect static files")
        return False
    
    # Populate database with sample data
    print("\n📊 Populating database with sample data...")
    populate_choice = input("Do you want to populate the database with sample dares? (y/n): ").lower()
    if populate_choice == 'y':
        if run_command(f"{activate_cmd} && python manage.py force_populate --settings={settings_module}", "Populating database"):
            print("✅ Database populated with sample data")
        else:
            print("⚠️  Warning: Failed to populate database, you can do this manually later")
    
    # Create superuser
    print("\n👤 Creating superuser account...")
    create_superuser = input("Do you want to create a superuser account now? (y/n): ").lower()
    if create_superuser == 'y':
        print("Please follow the prompts to create your superuser account:")
        os.system(f"source venv/bin/activate && python manage.py createsuperuser --settings={settings_module}")
    
    # Final instructions
    print("\n" + "=" * 60)
    print("🎉 DEPLOYMENT SETUP COMPLETE!")
    print("=" * 60)
    print("\n📋 Next steps:")
    print("1. Go to the PythonAnywhere Web tab")
    print("2. Create a new web app (Manual configuration, Python 3.11)")
    print("3. Set the WSGI file to the content of pythonanywhere_wsgi.py")
    print("4. Configure static files:")
    print(f"   - URL: /static/ → Directory: /home/{username}/dareproject/staticfiles")
    print(f"   - URL: /media/ → Directory: /home/{username}/dareproject/media")
    print("5. Set environment variables in the Web tab:")
    print(f"   - DJANGO_SETTINGS_MODULE: dareproject.pythonanywhere_settings")
    print("   - SECRET_KEY: (generate a secure secret key)")
    print("   - DEBUG: False")
    print("6. Reload your web app")
    print("\n🌐 Your app will be available at:")
    print(f"   https://{username}.pythonanywhere.com")
    print("\n📚 For detailed instructions, see: pythonanywhere_deployment_guide.md")
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        if success:
            print("\n✅ Deployment script completed successfully!")
        else:
            print("\n❌ Deployment script encountered errors.")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Deployment interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)