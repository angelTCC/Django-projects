from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response

def loginview(request):
    return render(request, 'login.html', {})

def registerview(request):
    return render(request, 'register.html', {})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    user = request.user
    return Response({
        "message": "Welcome to your profile!",
        "username": user.username,
        "email": user.email,
    })

