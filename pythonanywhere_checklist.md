# PythonAnywhere Deployment Checklist ✅

Use this checklist to ensure your Django Dare Exchange is properly deployed on PythonAnywhere.

## 📋 Pre-Deployment
- [ ] PythonAnywhere account created
- [ ] Project code uploaded to PythonAnywhere
- [ ] Located in `/home/yourusername/dareproject/` directory

## 🐍 Environment Setup
- [ ] Virtual environment created (`python3.11 -m venv venv`)
- [ ] Virtual environment activated (`source venv/bin/activate`)
- [ ] Dependencies installed (`pip install -r pythonanywhere_requirements.txt`)
- [ ] Pillow installed successfully (for image handling)

## ⚙️ Configuration
- [ ] `pythonanywhere_settings.py` updated with your username
- [ ] `pythonanywhere_wsgi.py` updated with your username
- [ ] SECRET_KEY generated and saved securely

## 🗄️ Database
- [ ] Migrations run (`python manage.py migrate --settings=dareproject.pythonanywhere_settings`)
- [ ] Sample data populated (`python manage.py force_populate --settings=dareproject.pythonanywhere_settings`)
- [ ] Superuser created (`python manage.py createsuperuser --settings=dareproject.pythonanywhere_settings`)
- [ ] Static files collected (`python manage.py collectstatic --settings=dareproject.pythonanywhere_settings --noinput`)

## 🌐 Web App Configuration
- [ ] New web app created (Manual configuration, Python 3.11)
- [ ] WSGI file configured with content from `pythonanywhere_wsgi.py`
- [ ] Static files mapping added: `/static/` → `/home/yourusername/dareproject/staticfiles`
- [ ] Media files mapping added: `/media/` → `/home/yourusername/dareproject/media`

## 🔐 Environment Variables
- [ ] `DJANGO_SETTINGS_MODULE` = `dareproject.pythonanywhere_settings`
- [ ] `SECRET_KEY` = Your generated secret key
- [ ] `DEBUG` = `False`

## 🚀 Final Steps
- [ ] Web app reloaded
- [ ] Site accessible at `yourusername.pythonanywhere.com`
- [ ] Admin panel accessible at `yourusername.pythonanywhere.com/admin/`
- [ ] Static files loading correctly (CSS/images)
- [ ] Sample dares visible on homepage

## 🧪 Testing
- [ ] Homepage loads without errors
- [ ] User registration works
- [ ] User login works
- [ ] Admin panel accessible
- [ ] Dare creation works
- [ ] Image uploads work (if using)
- [ ] All navigation links work

## 🔧 Troubleshooting
If something isn't working:

1. **Check the Error Log:**
   - Go to Web tab → Error log
   - Look for recent errors

2. **Common Issues:**
   - **Import errors:** Check virtual environment is activated
   - **Static files not loading:** Verify static files mapping
   - **Database errors:** Ensure migrations were run
   - **500 errors:** Check environment variables are set correctly

3. **Test Commands:**
   ```bash
   # Test settings
   python manage.py check --settings=dareproject.pythonanywhere_settings
   
   # Test database connection
   python manage.py shell --settings=dareproject.pythonanywhere_settings
   ```

## 📞 Support
- [PythonAnywhere Help](https://help.pythonanywhere.com/)
- [PythonAnywhere Forums](https://www.pythonanywhere.com/forums/)
- [Django Documentation](https://docs.djangoproject.com/)

---

**🎉 Congratulations!** If all items are checked, your Django Dare Exchange should be live and ready for users!

Your app is available at: `https://yourusername.pythonanywhere.com`

## Pre-Deployment
- [ ] Run `python setup_pythonanywhere.py` to configure files
- [ ] Update `pythonanywhere_wsgi.py` with your username
- [ ] Update `dareproject/pythonanywhere_settings.py` with your username
- [ ] Test your app locally with production settings

## PythonAnywhere Setup
- [ ] Create PythonAnywhere account
- [ ] Upload project files (Git or manual upload)
- [ ] Create virtual environment
- [ ] Install dependencies: `pip install -r pythonanywhere_requirements.txt`

## Web App Configuration
- [ ] Create new web app (Manual configuration)
- [ ] Select Python 3.11
- [ ] Update WSGI file with content from `pythonanywhere_wsgi.py`
- [ ] Configure static files:
  - URL: `/static/`
  - Directory: `/home/yourusername/Django/staticfiles`
- [ ] Configure media files:
  - URL: `/media/`
  - Directory: `/home/yourusername/Django/media`

## Environment Variables
- [ ] Set `DJANGO_SETTINGS_MODULE` to `dareproject.pythonanywhere_settings`
- [ ] Set `SECRET_KEY` to a secure value
- [ ] Set `DEBUG` to `False`

## Database Setup
- [ ] Run migrations: `python manage.py migrate --settings=dareproject.pythonanywhere_settings`
- [ ] Create superuser: `python manage.py createsuperuser --settings=dareproject.pythonanywhere_settings`
- [ ] Collect static files: `python manage.py collectstatic --settings=dareproject.pythonanywhere_settings --noinput`

## Final Steps
- [ ] Reload web app
- [ ] Test main page: `yourusername.pythonanywhere.com`
- [ ] Test admin: `yourusername.pythonanywhere.com/admin/`
- [ ] Check static files are loading
- [ ] Test all main functionality

## Troubleshooting
- [ ] Check error logs in Web tab
- [ ] Verify file permissions
- [ ] Ensure virtual environment is activated
- [ ] Check that all paths are correct

## Security
- [ ] Use strong secret key
- [ ] Set DEBUG=False
- [ ] Configure ALLOWED_HOSTS correctly
- [ ] Consider HTTPS (paid plan)

## Post-Deployment
- [ ] Set up regular backups
- [ ] Monitor error logs
- [ ] Keep dependencies updated
- [ ] Test after any code changes
