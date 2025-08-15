#!/usr/bin/env python3
"""
Deployment helper script for Django Dare Exchange project.
This script helps prepare your project for deployment.
"""

import os
import secrets
import string
from pathlib import Path

def generate_secret_key():
    """Generate a new Django secret key."""
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*(-_=+)"
    return ''.join(secrets.choice(alphabet) for _ in range(50))

def main():
    print("🚀 Django Dare Exchange - Deployment Helper")
    print("=" * 50)
    
    # Generate new secret key
    new_secret_key = generate_secret_key()
    print(f"\n🔑 New Secret Key Generated:")
    print(f"SECRET_KEY={new_secret_key}")
    
    print("\n📋 Environment Variables to Set:")
    print("=" * 30)
    print(f"SECRET_KEY={new_secret_key}")
    print("DEBUG=False")
    print("ALLOWED_HOSTS=your-domain.com,your-app-name.railway.app")
    print("DATABASE_URL=postgresql://... (will be set automatically by platform)")
    
    print("\n✅ Project is ready for deployment!")
    print("\n📖 Next steps:")
    print("1. Choose a hosting platform (Railway, Render, Heroku)")
    print("2. Push your code to GitHub")
    print("3. Connect your repository to the hosting platform")
    print("4. Set the environment variables above")
    print("5. Deploy!")
    
    print("\n📚 See DEPLOYMENT.md for detailed instructions.")
    
    # Check if all required files exist
    print("\n🔍 Checking deployment files:")
    required_files = [
        "requirements.txt",
        "Procfile", 
        "runtime.txt",
        "manage.py",
        "dareproject/settings.py"
    ]
    
    for file in required_files:
        if Path(file).exists():
            print(f"✅ {file}")
        else:
            print(f"❌ {file} (missing)")
    
    print("\n🎉 Ready to deploy!")

if __name__ == "__main__":
    main() 