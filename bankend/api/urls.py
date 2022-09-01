from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('authtoken/', obtain_auth_token),
    path('', views.api_home),
]
