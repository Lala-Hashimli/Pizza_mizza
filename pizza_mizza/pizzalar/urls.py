from django.urls import path
from .views import pizzaview


urlpatterns = [
    path("", pizzaview)
]