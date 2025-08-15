# 🚀 Deploy to Railway - Step by Step

Your Django project is ready to deploy! Follow these steps to get your live link:

## Step 1: Go to Railway
1. Open your browser and go to [railway.app](https://railway.app)
2. Click "Sign Up" and sign in with your GitHub account

## Step 2: Create New Project
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose your repository: `django-dare-exchange-app`
4. Railway will automatically detect it's a Django project

## Step 3: Add Database
1. In your Railway project dashboard, click "New"
2. Select "Database" → "PostgreSQL"
3. Railway will automatically set the `DATABASE_URL` environment variable

## Step 4: Set Environment Variables
1. Go to your project settings (gear icon)
2. Click "Variables" tab
3. Add these environment variables:
   ```
   SECRET_KEY=JXgKvSejs&M+fozkF98j)mSU)+dxa$6Yn#-s00nI^^LG-GYeQ=
   DEBUG=False
   ALLOWED_HOSTS=your-app-name.railway.app
   ```

## Step 5: Deploy
1. Railway will automatically deploy your app
2. You'll get a URL like: `https://your-app-name.railway.app`
3. Your app will be live in a few minutes!

## Step 6: Create Superuser
1. Go to your Railway project dashboard
2. Click on your web service
3. Go to "Deployments" tab
4. Click on the latest deployment
5. Click "View Logs"
6. In the terminal, run:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

## 🎉 Your App is Live!
Your Django Dare Exchange app will be accessible at the Railway URL!

## 🔗 Quick Links
- **Your GitHub Repo:** https://github.com/Rohith-Pavan/django-dare-exchange-app
- **Railway Dashboard:** https://railway.app/dashboard
- **Your Live App:** Will be available after deployment

## 📱 Features Available
- User registration and login
- Create and accept dares
- Rate completed dares
- User profiles
- Admin panel

## 🆘 Need Help?
- Check Railway logs for any errors
- Make sure all environment variables are set
- Verify the database is connected
- Test the app functionality

Your app will be live and ready to use once you complete these steps! 