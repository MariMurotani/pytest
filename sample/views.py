# for page
from django.shortcuts import render
from django.http import HttpResponse

# for API
import django_filters
from rest_framework import viewsets, filters
from .models import User
from .serializer import UserSerializer


# Create your views here.
# Page
def index(request):
    return HttpResponse("Hello, world. You're at the samples index.")

# API
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer