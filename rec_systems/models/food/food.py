from django.db import models

class Food(models.Model):
    food_id = models.CharField(default="", max_length=10, blank=True, null=True)
    name = models.CharField(default="", max_length=10, blank=True, null=True)
    class1 = models.CharField(default="", max_length=10, blank=True, null=True)
    class2 = models.CharField(default="", max_length=10, blank=True, null=True)
    position = models.CharField(default="", max_length=10, blank=True, null=True)
    price = models.CharField(default="", max_length=10, blank=True, null=True)
    imgUrl = models.URLField(max_length=256, blank=True)

    # 推荐 - 用户行为
    likes = models.IntegerField(default=0, blank=False, null=False) # 喜爱
    clicks = models.IntegerField(default=0, blank=False, null=False) # 点击
    collections = models.IntegerField(default=0, blank=False, null=False) # 收藏

    # 推荐 - 最相似的 k 个食物
    sim_food_topk = models.CharField(default="", max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.name)