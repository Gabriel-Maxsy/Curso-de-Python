from django.urls import path
# from home import views:
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name= 'home')
]