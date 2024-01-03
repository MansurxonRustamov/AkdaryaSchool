from django.urls import path
from .views import *
urlpatterns = [
    path("news/", newSchool, name='news')
]
