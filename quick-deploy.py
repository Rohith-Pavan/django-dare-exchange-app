#!/usr/bin/env python3
"""
Quick Deployment Script for Django Dare Exchange
This script will help you deploy your app and get a live link.
"""

import webbrowser
import time
import os

def main():
    print("🚀 Django Dare Exchange - Quick Deployment")
    print("=" * 50)
    
    print("\n✅ Your project is ready for deployment!")
    print("📁 GitHub Repository: https://github.com/Rohith-Pavan/django-dare-exchange-app")
    
    print("\n🔗 Let's deploy to Railway (Free hosting):")
    print("1. Opening Railway in your browser...")
    
    # Open Railway in browser
    webbrowser.open("https://railway.app")
    
    print("\n📋 Follow these steps:")
    print("1. Sign up/login to Railway with GitHub")
    print("2. Click 'New Project'")
    print("3. Select 'Deploy from GitHub repo'")
    print("4. Choose: django-dare-exchange-app")
    print("5. Railway will auto-detect Django and deploy!")
    
    print("\n⚙️ Environment Variables to set:")
    print("SECRET_KEY=JXgKvSejs&M+fozkF98j)mSU)+dxa$6Yn#-s00nI^^LG-GYeQ=")
    print("DEBUG=False")
    print("ALLOWED_HOSTS=your-app-name.railway.app")
    
    print("\n🗄️ Add PostgreSQL Database:")
    print("1. In Railway dashboard, click 'New'")
    print("2. Select 'Database' → 'PostgreSQL'")
    print("3. Railway will auto-set DATABASE_URL")
    
    print("\n⏳ Deployment will take 2-5 minutes...")
    print("🎉 You'll get a live URL like: https://your-app-name.railway.app")
    
    print("\n🔧 After deployment, create admin user:")
    print("1. Go to your Railway project")
    print("2. Click on web service")
    print("3. Go to 'Deployments' → 'View Logs'")
    print("4. Run: python manage.py migrate")
    print("5. Run: python manage.py createsuperuser")
    
    print("\n📱 Your app features:")
    print("• User registration & login")
    print("• Create & accept dares")
    print("• Rate completed dares")
    print("• User profiles")
    print("• Admin panel")
    
    print("\n🎯 Alternative: Deploy to Render")
    print("If Railway doesn't work, try: https://render.com")
    
    input("\nPress Enter when you're ready to start deployment...")
    
    print("\n🚀 Good luck! Your app will be live soon!")
    print("📞 Need help? Check the logs in Railway dashboard.")

if __name__ == "__main__":
    main() 