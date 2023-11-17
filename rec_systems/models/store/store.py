from django.db import models

class Store(models.Model):
    store_id = models.CharField(default="", max_length=10, blank=True, null=True)
    name = models.CharField(default="", max_length=10, blank=True, null=True)
    open_time = models.CharField(default="", max_length=10, blank=True, null=True)
    stars = models.CharField(default="", max_length=10, blank=True, null=True)
    category = models.CharField(default="", max_length=10, blank=True, null=True)
    img1 = models.URLField(max_length=256, blank=True)
    img2 = models.URLField(max_length=256, blank=True)
    img3 = models.URLField(max_length=256, blank=True)

    def __str__(self):
        return str(self.name)