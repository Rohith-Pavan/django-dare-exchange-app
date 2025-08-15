# Django Dare Exchange - Deployment Guide

This guide will help you deploy your Django Dare Exchange project to various hosting platforms.

## 🚀 Quick Deploy Options

### Option 1: Railway (Recommended - Easiest)

1. **Sign up for Railway**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub

2. **Deploy from GitHub**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway will automatically detect it's a Django project

3. **Set Environment Variables**
   - Go to your project settings
   - Add these environment variables:
     ```
     SECRET_KEY=your-secret-key-here
     DEBUG=False
     ALLOWED_HOSTS=your-app-name.railway.app
     ```

4. **Add Database**
   - In Railway dashboard, click "New"
   - Select "Database" → "PostgreSQL"
   - Railway will automatically set the `DATABASE_URL` environment variable

5. **Deploy**
   - Railway will automatically deploy when you push to GitHub
   - Your app will be available at `https://your-app-name.railway.app`

### Option 2: Render

1. **Sign up for Render**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub

2. **Create New Web Service**
   - Click "New" → "Web Service"
   - Connect your GitHub repository

3. **Configure the service:**
   - **Name:** dare-exchange
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn dareproject.wsgi:application`

4. **Set Environment Variables:**
   - `SECRET_KEY`: Generate a new secret key
   - `DEBUG`: False
   - `ALLOWED_HOSTS`: your-app-name.onrender.com

5. **Add Database**
   - Create a new PostgreSQL database in Render
   - Render will automatically set `DATABASE_URL`

### Option 3: Heroku

1. **Install Heroku CLI**
   ```bash
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku app**
   ```bash
   heroku create your-app-name
   ```

4. **Add PostgreSQL database**
   ```bash
   heroku addons:create heroku-postgresql:mini
   ```

5. **Set environment variables**
   ```bash
   heroku config:set SECRET_KEY=your-secret-key-here
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
   ```

6. **Deploy**
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

7. **Run migrations**
   ```bash
   heroku run python manage.py migrate
   ```

8. **Create superuser**
   ```bash
   heroku run python manage.py createsuperuser
   ```

## 🔧 Pre-deployment Checklist

Before deploying, make sure you have:

- [ ] Updated `requirements.txt` with all dependencies
- [ ] Created `Procfile` for the web server
- [ ] Updated `settings.py` for production
- [ ] Generated a new `SECRET_KEY`
- [ ] Set `DEBUG=False` for production
- [ ] Configured database settings
- [ ] Set up static file handling

## 🔑 Generate a New Secret Key

For production, generate a new secret key:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

## 📁 Project Structure for Deployment

Your project should have these files for deployment:

```
Django/
├── dareproject/
│   ├── settings.py      # Updated for production
│   ├── urls.py
│   └── wsgi.py
├── dare/                # Your app
├── templates/
├── static/
├── requirements.txt     # All dependencies
├── Procfile            # For gunicorn
├── runtime.txt         # Python version
├── manage.py
└── .gitignore
```

## 🌐 Domain and SSL

Most platforms provide:
- **Automatic SSL certificates**
- **Custom domain support**
- **CDN for static files**

## 📊 Monitoring and Logs

After deployment:
- Check your platform's dashboard for logs
- Monitor application performance
- Set up error tracking (optional)

## 🔄 Continuous Deployment

To enable automatic deployments:
1. Connect your GitHub repository
2. Set up webhooks
3. Push changes to trigger automatic deployment

## 🆘 Troubleshooting

### Common Issues:

1. **Static files not loading**
   - Run `python manage.py collectstatic`
   - Check `STATIC_ROOT` and `STATIC_URL` settings

2. **Database connection errors**
   - Verify `DATABASE_URL` environment variable
   - Check database credentials

3. **500 Internal Server Error**
   - Check application logs
   - Verify all environment variables are set
   - Ensure `DEBUG=False` in production

4. **Migration errors**
   - Run `python manage.py migrate` manually
   - Check database permissions

### Getting Help:

- Check your platform's documentation
- Review application logs
- Test locally with production settings

## 🎉 Success!

Once deployed, your Django Dare Exchange app will be live and accessible to users worldwide!

**Remember to:**
- Create a superuser account
- Test all functionality
- Monitor performance
- Keep dependencies updated 