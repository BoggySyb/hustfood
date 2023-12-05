from django.db import models
from datetime import date

class Usercf_rec(models.Model):
    user_name = models.CharField(default="", max_length=10, blank=True, null=True)
    rec_food_ids = models.CharField(default="", max_length=200, blank=True, null=True)

    def __str__(self):
        return str(date.today()) + " For " + str(self.user_name)