# Django Dare Exchange - Netlify Deployment Guide

## Overview

This guide explains how to deploy your Django Dare Exchange application to Netlify using serverless functions.

## Important Notes

⚠️ **Limitations of Netlify for Django:**
- Netlify is primarily designed for static sites and JAMstack applications
- Django is a server-side framework that requires persistent server processes
- This deployment uses Netlify Functions (serverless) which has limitations:
  - Cold start delays
  - 10-second execution timeout
  - Limited database persistence
  - No background tasks

## Files Created for Netlify Deployment

### 1. `netlify.toml`
Configuration file that tells Netlify how to build and deploy your app:
- Sets build command to `python build.py`
- Configures redirects to route requests to Django serverless function
- Sets environment variables

### 2. `netlify/functions/django-app.py`
Serverless function that wraps your Django application:
- Handles HTTP requests and converts them to Django format
- Processes requests through Django WSGI application
- Returns responses in Netlify-compatible format

### 3. `build.py`
Build script that prepares your Django app for deployment:
- Installs dependencies
- Runs database migrations
- Creates admin user
- Collects static files

### 4. `index.html`
Static fallback page that redirects to the Django function

## Deployment Steps

### Step 1: Push to GitHub
Ensure all files are committed and pushed to your GitHub repository.

### Step 2: Connect to Netlify
1. Go to [netlify.com](https://netlify.com) and sign up/login
2. Click "New site from Git"
3. Choose GitHub and select your repository
4. Netlify will automatically detect the `netlify.toml` configuration

### Step 3: Configure Environment Variables
In Netlify dashboard, go to Site settings > Environment variables and add:
```
NETLIFY=1
DJANGO_SETTINGS_MODULE=dareproject.settings
SECRET_KEY=your-secret-key-here
DEBUG=False
```

### Step 4: Deploy
Netlify will automatically build and deploy your site.

## Expected Behavior

### What Works:
- ✅ Basic Django views and templates
- ✅ Static file serving
- ✅ Simple database operations (SQLite in /tmp)
- ✅ Authentication (session-based)
- ✅ Admin panel access

### What May Not Work:
- ❌ Complex database operations (data doesn't persist between function calls)
- ❌ File uploads (no persistent storage)
- ❌ Background tasks
- ❌ WebSocket connections
- ❌ Long-running processes

## Accessing Your App

Once deployed:
- **Main app**: `https://your-site-name.netlify.app/`
- **Admin panel**: `https://your-site-name.netlify.app/admin/`
- **Health check**: `https://your-site-name.netlify.app/health/`

## Admin Access
The build script creates an admin user:
- **Username**: `admin`
- **Password**: `admin123`
- **Email**: `admin@example.com`

⚠️ **Security**: Change these credentials immediately after deployment!

## Troubleshooting

### Common Issues:

1. **Function Timeout**
   - Netlify functions have a 10-second timeout
   - Optimize database queries and reduce processing time

2. **Database Issues**
   - Data doesn't persist between function calls
   - Consider using external database services (PostgreSQL on Heroku, etc.)

3. **Static Files Not Loading**
   - Check that `collectstatic` ran successfully during build
   - Verify redirect rules in `netlify.toml`

4. **Cold Start Delays**
   - First request after inactivity may be slow
   - This is normal for serverless functions

## Alternative Recommendations

For a full Django application, consider these alternatives:

1. **Railway** (Current deployment) - Better for Django apps
2. **Heroku** - Traditional Django hosting
3. **DigitalOcean App Platform** - Good Django support
4. **AWS Elastic Beanstalk** - Scalable Django hosting
5. **Google Cloud Run** - Containerized Django deployment

## Conclusion

While it's possible to deploy Django to Netlify using serverless functions, it's not the ideal platform for Django applications. The serverless approach works best for simple, stateless applications.

For your Django Dare Exchange app, Railway (your current deployment) is likely a better choice as it provides:
- Persistent database storage
- No execution time limits
- Better Django compatibility
- Easier deployment process

Use this Netlify deployment as a backup or for testing purposes, but consider Railway or other Django-friendly platforms for production use.