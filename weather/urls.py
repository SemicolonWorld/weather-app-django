from django.conf.urls import url
from django.urls import path
from .views import weather

app_name = 'weather'

urlpatterns = [
    path('', weather, name='weather_get'),
]
