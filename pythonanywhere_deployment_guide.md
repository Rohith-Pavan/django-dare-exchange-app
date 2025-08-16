# PythonAnywhere Deployment Guide for Django Dare Exchange

## 🚀 Quick Start (Automated)

For the fastest deployment, use our automated script:

1. Upload your project to PythonAnywhere
2. Open a Bash console and navigate to your project directory
3. Run: `python3 deploy_pythonanywhere.py`
4. Follow the prompts and complete the web app configuration

## 📋 Prerequisites
1. A PythonAnywhere account (free or paid)
2. Your Django Dare Exchange project code
3. Basic familiarity with command line

## 📁 Step 1: Upload Your Project

### Option A: Using Git (Recommended)
1. In PythonAnywhere, open a **Bash console**
2. Navigate to your home directory:
   ```bash
   cd ~
   ```
3. Clone your Django Dare Exchange repository:
   ```bash
   git clone https://github.com/yourusername/django-dare-exchange-app.git dareproject
   ```
4. Navigate to your project:
   ```bash
   cd dareproject
   ```

### Option B: Manual Upload
1. Download your project as a ZIP file
2. In PythonAnywhere, go to **Files** tab
3. Upload the ZIP file to your home directory
4. Extract it using the Bash console:
   ```bash
   cd ~
   unzip django-dare-exchange-app.zip
   mv django-dare-exchange-app dareproject
   cd dareproject
   ```

## 🐍 Step 2: Set Up Virtual Environment

1. Create a virtual environment:
   ```bash
   cd ~/dareproject
   python3.11 -m venv venv
   ```

2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

3. Upgrade pip and install dependencies:
   ```bash
   pip install --upgrade pip
   pip install -r pythonanywhere_requirements.txt
   ```

**Note:** If you get errors installing Pillow, you may need to install it separately:
```bash
pip install Pillow
```

## ⚙️ Step 3: Configure Settings

### Automated Configuration (Recommended)
If you used the deployment script, this is already done. Otherwise:

1. **Update configuration files manually:**
   - In `pythonanywhere_settings.py`: Replace `yourusername` with your actual PythonAnywhere username
   - In `pythonanywhere_wsgi.py`: Replace `yourusername` with your actual PythonAnywhere username

2. **Generate a secure SECRET_KEY:**
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```
   Save this key for the web app environment variables.

## 🗄️ Step 4: Set Up Database

1. **Run migrations:**
   ```bash
   python manage.py migrate --settings=dareproject.pythonanywhere_settings
   ```

2. **Populate with sample data (optional but recommended):**
   ```bash
   python manage.py force_populate --settings=dareproject.pythonanywhere_settings
   ```
   This creates sample dares, categories, and demo users.

3. **Create a superuser:**
   ```bash
   python manage.py createsuperuser --settings=dareproject.pythonanywhere_settings
   ```

4. **Collect static files:**
   ```bash
   python manage.py collectstatic --settings=dareproject.pythonanywhere_settings --noinput
   ```

## 🌐 Step 5: Configure Web App

1. Go to the **Web** tab in PythonAnywhere dashboard
2. Click **Add a new web app**
3. Choose **Manual configuration** (not Django)
4. Select **Python 3.11**
5. Click **Next** to create the app

### Configure WSGI File
1. In the **Code** section, click on the **WSGI configuration file** link
2. **Delete all existing content** in the file
3. Copy and paste the entire content from your `pythonanywhere_wsgi.py` file
4. Make sure `yourusername` is replaced with your actual username
5. **Save** the file

### Configure Static Files
1. In the **Static files** section, click **Add a new static files mapping**:
   - **URL:** `/static/`
   - **Directory:** `/home/yourusername/dareproject/staticfiles`

2. Add another mapping for media files:
   - **URL:** `/media/`
   - **Directory:** `/home/yourusername/dareproject/media`

**Replace `yourusername` with your actual PythonAnywhere username!**

## 🔐 Step 6: Set Environment Variables

1. In the **Web** tab, scroll down to **Environment variables**
2. Click **Add a new environment variable** and add:
   - **Name:** `DJANGO_SETTINGS_MODULE`
   - **Value:** `dareproject.pythonanywhere_settings`

3. Add another environment variable:
   - **Name:** `SECRET_KEY`
   - **Value:** Your secure secret key (generated in Step 3)

4. Add a third environment variable:
   - **Name:** `DEBUG`
   - **Value:** `False`

**Important:** Keep your SECRET_KEY secure and never share it publicly!

## Step 7: Reload Web App

1. Click the **Reload** button in the Web tab
2. Your app should now be live at `yourusername.pythonanywhere.com`

## Step 8: Test Your Application

1. Visit your domain to ensure the app is working
2. Test the admin interface at `yourusername.pythonanywhere.com/admin/`
3. Check that static files are loading correctly

## Troubleshooting

### Common Issues:

1. **Import Errors**: Make sure your virtual environment is activated and dependencies are installed
2. **Static Files Not Loading**: Check that `collectstatic` was run and static files are configured correctly
3. **Database Errors**: Ensure migrations are up to date
4. **Permission Errors**: Check file permissions in your project directory

### Debugging:
1. Check the error logs in the **Web** tab
2. Use the **Files** tab to examine log files
3. Test your app locally with the same settings

## Security Considerations

1. **Secret Key**: Use a strong, unique secret key
2. **DEBUG**: Always set to `False` in production
3. **ALLOWED_HOSTS**: Only include your actual domain
4. **HTTPS**: Consider upgrading to a paid plan for HTTPS support

## Maintenance

1. **Regular Updates**: Keep Django and dependencies updated
2. **Backups**: Regularly backup your database and code
3. **Monitoring**: Check error logs regularly
4. **Performance**: Monitor your app's performance and optimize as needed

## Additional Resources

- [PythonAnywhere Help](https://help.pythonanywhere.com/)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/)
- [PythonAnywhere Django Tutorial](https://tutorial.djangogirls.org/en/deploy/)
