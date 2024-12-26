from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/', views.loginview, name='login'),
    path('secret/', views.secret),
    path('api-token-auth/', obtain_auth_token),
]