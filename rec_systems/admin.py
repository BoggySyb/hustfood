from django.contrib import admin
from rec_systems.models.food.food import Food
from rec_systems.models.store.store import Store
from rec_systems.models.appuser.appuser import AppUser
from rec_systems.models.log.log import Log
from rec_systems.models.recommend.recommend import Usercf_rec


# Register your models here.
admin.site.register(Food)
admin.site.register(Store)
admin.site.register(AppUser)
admin.site.register(Log)
admin.site.register(Usercf_rec)