import requests
from django.shortcuts import render
from django.views import View


class DriverView(View):
    def get(self, request):
        response = requests.get('https://fastapi-getir-39bf7a2f1f3a.herokuapp.com/drivers/')
        if response.status_code == 200:
            data = response.json()
            drivers = data["records"]
        else:
            drivers = []  # Empty list if response not successful

        context = {
            'drivers': drivers
        }
        return render(request, 'driver/home.html', context)
