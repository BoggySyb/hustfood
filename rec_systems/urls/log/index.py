from django.urls import path
from rec_systems.views.log.record_log import record_log

urlpatterns = [
    path('', record_log, name="record_log"),
]