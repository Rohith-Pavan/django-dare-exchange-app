import json
import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dareproject.settings')

import django
from django.core.wsgi import get_wsgi_application
from django.http import HttpRequest
from django.test import RequestFactory

# Initialize Django
django.setup()
application = get_wsgi_application()

def handler(event, context):
    """
    Netlify serverless function handler for Django
    """
    try:
        # Extract request information from Netlify event
        http_method = event.get('httpMethod', 'GET')
        path = event.get('path', '/')
        query_string = event.get('queryStringParameters') or {}
        headers = event.get('headers', {})
        body = event.get('body', '')
        
        # Create Django request
        factory = RequestFactory()
        
        if http_method == 'GET':
            request = factory.get(path, query_string)
        elif http_method == 'POST':
            request = factory.post(path, data=body, content_type=headers.get('content-type', 'application/json'))
        elif http_method == 'PUT':
            request = factory.put(path, data=body, content_type=headers.get('content-type', 'application/json'))
        elif http_method == 'DELETE':
            request = factory.delete(path)
        else:
            request = factory.generic(http_method, path, data=body)
        
        # Add headers to request
        for key, value in headers.items():
            request.META[f'HTTP_{key.upper().replace("-", "_")}'] = value
        
        # Process request through Django
        response = application(request.META, lambda status, headers: None)
        
        # Convert Django response to Netlify format
        response_body = b''.join(response).decode('utf-8')
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/html',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS'
            },
            'body': response_body
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': str(e),
                'message': 'Internal server error'
            })
        }