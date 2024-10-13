from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import ThreadsToken
from .utils import get_threads_token

@login_required
def threads_authorize(request):
    authorize_url = f"https://threads.net/oauth/authorize?client_id={settings.THREADS_CLIENT_ID}&redirect_uri={settings.THREADS_REDIRECT_URI}&scope=threads_basic,threads_content_publish"
    return redirect(authorize_url)

@login_required
def threads_callback(request):
    code = request.GET.get('code')
    if code:
        token_data = get_threads_token(code)
        if token_data:
            ThreadsToken.objects.update_or_create(
                user=request.user,
                defaults={
                    'access_token': token_data['access_token'],
                    'refresh_token': token_data['refresh_token'],
                    'expires_at': token_data['expires_at']
                }
            )
            return redirect('home')  # 또는 다른 적절한 페이지로 리다이렉트
    return render(request, 'threads_auth/error.html', {'message': 'Failed to authenticate with Threads'})