from django.urls import path
from .views import DriverView

urlpatterns = [
    path('', DriverView.as_view(), name='driver'),
]
