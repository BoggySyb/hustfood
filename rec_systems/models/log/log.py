from django.db import models
from django.utils.timezone import now

class Log(models.Model):
    user_name = models.CharField(default="", max_length=10, blank=True, null=True)
    food_id = models.CharField(default="", max_length=10, blank=True, null=True)
    action_time = models.TimeField(default=now, blank=False)
    action_type = models.CharField(default="", max_length=10, blank=True, null=True)
