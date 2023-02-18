#https://blog.devgenius.io/django-and-flutter-a-step-by-step-tutorial-for-a-boilerplate-application-f564335f2e8b
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response 
from rest_framework.permissions import AllowAny 
from rest_framework.decorators import api_view, permission_classes 

# Create your views here.
@api_view([
    'GET'
],)
@permission_classes([AllowAny],)

def hellobiyatch(request):
    return HttpResponse("hello biyatch")