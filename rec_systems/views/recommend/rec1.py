from django.http import JsonResponse
from rec_systems.models.food.food import Food
from django.core.cache import cache
import random

def foodData(food):
    return {
        'name': food.name,
        'class1': food.class1,
        'class2': food.class2,
        'position': food.position,
        'price': food.price,
        'imgUrl': food.imgUrl,
    }

def recommend(request):
    event = request.GET.get('event')
    if event == "rec":
        user = request.user
        food_id = random.choice(cache.get('user_rec_list')[user.username])
        food = Food.objects.all().get(food_id=food_id)
        return JsonResponse({
            'result': "success",
            'data': foodData(food),
        })
    else:
        return JsonResponse({
            'result': "fail",
        })