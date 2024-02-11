import requests
from django.shortcuts import render
from django.views import View


class DriverView(View):
    def get(self, request):
        response = requests.get('http://localhost:8000/')
        if response.status_code == 200:
            data = response.json()
            drivers = data["records"]
        else:
            drivers = []  # Empty list if response not successful

        context = {
            'drivers': drivers
        }
        return render(request, 'driver/home.html', context)
