from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/', views.loginview, name='loginview'),
    path('register/', views.registerview, name='registerview'),
    path('profile/', views.profile_view, name='profile'),
    path('api-token-auth/', obtain_auth_token), # create and get token if you have one acount
]

# http://127.0.01:8000/auth/users/ # user will be created without send token

