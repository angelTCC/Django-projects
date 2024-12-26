from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response

def loginview(request):
    return render(request, 'login.html', {})

@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({'message':'some secret message'})
