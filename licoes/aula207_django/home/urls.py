from django.urls import path
# from home import views:
from . import views

urlpatterns = [
    path('', views.home)
]