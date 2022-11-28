
from apps.cars.views import CarListCrateView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('cars',CarListCrateView.as_view()),
]
