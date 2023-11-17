from django.urls import path, include

urlpatterns = [
    path('rec/', include("rec_systems.urls.recommend.index")),
    path('msg/', include("rec_systems.urls.message.index")),
]