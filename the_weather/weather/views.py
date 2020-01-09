import requests
from django.shortcuts import render, get_object_or_404, redirect
from .models import City
from .form import CityForm


def index(request):
	cities=City.objects.all()
	url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=7b67c8dc56b6e5745aa72c697087c786&lang=ru'

	if request.method == "POST":
		
		city = request.POST['name']
		r = requests.get(url.format(city)).status_code

		if City.objects.filter(name = request.POST['name']).count()<1 and r != 404:
			form = CityForm(request.POST)
			form.save() 
	
	form = CityForm()
	weather_data = []
	
	for city in cities:
		
		r=requests.get(url.format(city)).json()

		data = {
			'city' : city,
			'temperature' : r['main']['temp'],
			'description' : r['weather'][0]['description'],
			'icon' :r['weather'][0]['icon'],
		}
		weather_data.append(data)

	context = {'weather_data' : weather_data, 'form' : form}
	return render(request, 'weather.html', context)
	

def city_delete(request, name):
	print(name)
	city=get_object_or_404(City, name=name)
	city.delete()
	return redirect('/')
    