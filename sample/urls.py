# coding: utf-8
# Page
from django.conf.urls import url
from . import views

# API
from rest_framework import routers
from .views import UserViewSet

# Page
urlpatterns = [
   url(r'^$', views.index, name='index'),
]

# API
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
