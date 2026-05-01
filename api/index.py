# Vercel serverless handler
import os
import sys

# Add project to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.wsgi import application

# Vercel expects 'handler' function
def handler(request, **kwargs):
    return application(request.environ, request.start_response)
