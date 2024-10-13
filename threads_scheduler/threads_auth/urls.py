from django.urls import path
from . import views

urlpatterns = [
    path('authorize/', views.threads_authorize, name='threads_authorize'),
    path('callback/', views.threads_callback, name='threads_callback'),
]