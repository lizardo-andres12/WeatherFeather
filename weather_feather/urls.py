"""URLs patterns for weather_feather"""

from django.urls import path
from . import views

# Define namespace for views
appname = 'wf'
urlpatterns = [
    path('', views.index, name='home')

]
