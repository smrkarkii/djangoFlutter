from django.urls import path
from . import views

urlpatterns=[
    path('hellobiyatch', views.hellobiyatch, name ="hellobiyatch")
]