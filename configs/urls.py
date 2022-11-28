
from apps.cars.views import CarListCrateView,CarRetriveUpdateDestroyViev
from django.urls import path

urlpatterns = [
    path('cars',CarListCrateView.as_view()),
    path('cars/<int:pk>',CarRetriveUpdateDestroyViev.as_view())
]
