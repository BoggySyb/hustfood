from django.urls import path
from rec_systems.views.message.getFoods import getFoods
from rec_systems.views.message.getStores import getStores

urlpatterns = [
    path('getFoods/', getFoods, name="getFoods"),
    path('getStores/', getStores, name="getStores"),
]