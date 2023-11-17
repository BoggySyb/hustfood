from django.urls import path
from rec_systems.views.recommend.first_try import first_try
from rec_systems.views.recommend.rec1 import recommend as rec1
from rec_systems.views.recommend.rec2 import recommend as rec2

urlpatterns = [
    path('try/', first_try, name="first_try"),
    path('rec1/', rec1, name="rec1"),
    path('rec2/', rec2, name="rec2"),
]