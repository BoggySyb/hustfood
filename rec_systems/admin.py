from django.contrib import admin
from rec_systems.models.food.food import Food
from rec_systems.models.store.store import Store

# Register your models here.
admin.site.register(Food)
admin.site.register(Store)