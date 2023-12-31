from django.urls import path
from rec_systems.views.setting.login import signin
from rec_systems.views.setting.register import register
from rec_systems.views.setting.getinfo import getinfo
from rec_systems.views.setting.logout import signout

urlpatterns = [
    path('login/', signin, name="login"),
    path('register/', register, name="register"),
    path('getinfo/', getinfo, name="getinfo"),
    path('logout/', signout, name="logout"),
]