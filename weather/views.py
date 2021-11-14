from django.shortcuts import render
import requests as re
import time
from .forms import CityForm

# Create your views here.

def celsius_to_fahrenheit(cel_number):
    return cel_number * 1.8 + 32

def weather(request):
    # get city section
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = request.POST['city']
            # get weather section
            URL = 'https://api.openweathermap.org/data/2.5/weather'
            PARAMS = {
                'q': city,
                'appid': 'ab5f0bf24a1da23698500bcf5677febf',
                'units': 'metric',
            }
            data = re.get(url=URL, params=PARAMS)
            info = data.json()
        try:
            if 'weather' in info:    
                context = {
                    'form': form,
                    'main': info['weather'][0]['main'],
                    'description': info['weather'][0]['description'],
                    'icon': info['weather'][0]['icon'],
                    'celsius_temp': round(float(info['main']['temp'])),
                    'country': info['sys']['country'].lower(),
                    'humidity': info['main']['humidity'],
                    'city_name': info['name'],
                }
            elif 'cod' in info and 'message' in info:
                context = {
                    'form': form,
                    'cod': info['cod'],
                    'message': info['message'],
                }
        except:
            context = {
                'form': form
            }
    else:
        form = CityForm()
        context = {
            'form': form,
        }
    
    return render(request, 'weather/index.html', context)