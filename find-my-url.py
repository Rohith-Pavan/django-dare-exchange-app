#!/usr/bin/env python3
"""
Find My URL - Step by Step Deployment Guide
This script will help you deploy and find your live URL.
"""

import webbrowser
import time

def main():
    print("🔍 Find My URL - Django Deployment Helper")
    print("=" * 50)
    
    print("\n❓ Have you deployed to Railway or Render yet?")
    print("1. Yes, I deployed but can't find the URL")
    print("2. No, I haven't deployed yet")
    
    choice = input("\nEnter your choice (1 or 2): ").strip()
    
    if choice == "1":
        help_find_url()
    elif choice == "2":
        help_deploy()
    else:
        print("Invalid choice. Let me help you deploy first.")
        help_deploy()

def help_deploy():
    print("\n🚀 Let's Deploy Your App!")
    print("=" * 30)
    
    print("\n📋 Choose your platform:")
    print("1. Railway (Recommended - Free)")
    print("2. Render (Alternative - Free)")
    
    platform = input("\nWhich platform? (1 or 2): ").strip()
    
    if platform == "1":
        deploy_railway()
    elif platform == "2":
        deploy_render()
    else:
        print("Invalid choice. Using Railway...")
        deploy_railway()

def deploy_railway():
    print("\n🚂 Deploying to Railway...")
    print("1. Opening Railway in your browser...")
    webbrowser.open("https://railway.app")
    
    print("\n📋 Follow these exact steps:")
    print("1. Sign up/login with GitHub")
    print("2. Click 'New Project'")
    print("3. Select 'Deploy from GitHub repo'")
    print("4. Choose: django-dare-exchange-app")
    print("5. Wait for deployment to complete")
    print("6. Look for the blue URL button at the top!")
    
    print("\n⚙️ Environment Variables (set these in Railway):")
    print("SECRET_KEY=JXgKvSejs&M+fozkF98j)mSU)+dxa$6Yn#-s00nI^^LG-GYeQ=")
    print("DEBUG=False")
    print("ALLOWED_HOSTS=your-app-name.railway.app")
    
    print("\n🗄️ Add Database:")
    print("1. In Railway dashboard, click 'New'")
    print("2. Select 'Database' → 'PostgreSQL'")
    
    input("\nPress Enter when you've completed these steps...")
    help_find_url()

def deploy_render():
    print("\n🎨 Deploying to Render...")
    print("1. Opening Render in your browser...")
    webbrowser.open("https://render.com")
    
    print("\n📋 Follow these exact steps:")
    print("1. Sign up/login with GitHub")
    print("2. Click 'New' → 'Web Service'")
    print("3. Connect your GitHub repo: django-dare-exchange-app")
    print("4. Set Build Command: pip install -r requirements.txt")
    print("5. Set Start Command: gunicorn dareproject.wsgi:application")
    print("6. Click 'Create Web Service'")
    print("7. Wait for deployment to complete")
    
    input("\nPress Enter when you've completed these steps...")
    help_find_url()

def help_find_url():
    print("\n🔍 Finding Your URL...")
    print("=" * 30)
    
    print("\n📍 Where to look for your URL:")
    
    print("\n🚂 If you used Railway:")
    print("1. Go to https://railway.app/dashboard")
    print("2. Click on your project (django-dare-exchange-app)")
    print("3. Look for a BIG BLUE BUTTON with your URL")
    print("4. It should look like: https://django-dare-exchange-app-production-xxxx.up.railway.app")
    
    print("\n🎨 If you used Render:")
    print("1. Go to https://dashboard.render.com")
    print("2. Click on your web service (dare-exchange)")
    print("3. Look for 'URL' in the service overview")
    print("4. It should look like: https://dare-exchange.onrender.com")
    
    print("\n❓ Still can't find it?")
    print("1. Check if deployment is still in progress")
    print("2. Look for any error messages")
    print("3. Try refreshing the page")
    
    print("\n🔗 Quick Links:")
    print("- Railway Dashboard: https://railway.app/dashboard")
    print("- Render Dashboard: https://dashboard.render.com")
    print("- Your GitHub Repo: https://github.com/Rohith-Pavan/django-dare-exchange-app")
    
    input("\nPress Enter when you find your URL...")
    
    print("\n🎉 Great! Your Django app should now be live!")
    print("📱 Test your app by:")
    print("1. Opening the URL in your browser")
    print("2. Creating a new user account")
    print("3. Exploring the dare features")

if __name__ == "__main__":
    main() 