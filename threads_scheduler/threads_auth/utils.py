import requests
from django.conf import settings
from django.utils import timezone
from datetime import timedelta

def get_threads_token(code):
    token_url = "https://graph.threads.net/oauth/access_token"
    data = {
        'client_id': settings.THREADS_CLIENT_ID,
        'client_secret': settings.THREADS_CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'redirect_uri': settings.THREADS_REDIRECT_URI,
        'code': code
    }
    response = requests.post(token_url, data=data)
    if response.status_code == 200:
        token_data = response.json()
        expires_in = token_data.get('expires_in', 3600)
        expires_at = timezone.now() + timedelta(seconds=expires_in)
        return {
            'access_token': token_data['access_token'],
            'refresh_token': token_data.get('refresh_token'),
            'expires_at': expires_at
        }
    return None

def refresh_threads_token(refresh_token):
    token_url = "https://graph.threads.net/oauth/access_token"
    data = {
        'client_id': settings.THREADS_CLIENT_ID,
        'client_secret': settings.THREADS_CLIENT_SECRET,
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }
    response = requests.post(token_url, data=data)
    if response.status_code == 200:
        token_data = response.json()
        expires_in = token_data.get('expires_in', 3600)
        expires_at = timezone.now() + timedelta(seconds=expires_in)
        return {
            'access_token': token_data['access_token'],
            'refresh_token': token_data.get('refresh_token', refresh_token),
            'expires_at': expires_at
        }
    return None