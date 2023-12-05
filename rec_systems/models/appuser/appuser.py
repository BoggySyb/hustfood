from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.URLField(max_length=256, blank=True)
    created_time = models.DateTimeField(default=now, blank=False)
    is_new_user = models.BooleanField(default=True)

    # 推荐相关
    near_pos  = models.CharField(default="", max_length=10, blank=True, null=True)
    favour_class = models.CharField(default="", max_length=10, blank=True, null=True)

    def __str__(self):
        return str(self.user)