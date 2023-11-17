from django.db import models

class Food(models.Model):
    food_id = models.CharField(default="", max_length=10, blank=True, null=True)
    name = models.CharField(default="", max_length=10, blank=True, null=True)
    class1 = models.CharField(default="", max_length=10, blank=True, null=True)
    class2 = models.CharField(default="", max_length=10, blank=True, null=True)
    position = models.CharField(default="", max_length=10, blank=True, null=True)
    price = models.CharField(default="", max_length=10, blank=True, null=True)
    imgUrl = models.URLField(max_length=256, blank=True)

    def __str__(self):
        return str(self.name)