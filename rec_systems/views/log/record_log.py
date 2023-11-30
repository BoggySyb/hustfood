from django.http import JsonResponse
from rec_systems.models.log.log import Log
from rec_systems.models.food.food import Food
from django.utils.timezone import now, localtime
def record_log(request):
    user_name = request.user.username
    food_id = request.GET.get('food_id')
    action_type = request.GET.get('event')
    Log.objects.all().create(user_name=user_name, food_id=food_id, action_type=action_type, action_time=localtime(now()))

    food = Food.objects.all().get(food_id=food_id)
    if action_type == "click":
        food.clicks += 1
        food.save()
    elif action_type == "like":
        food.likes += 1
        food.save()
    elif action_type == "unlike":
        food.likes -= 1
        food.save()
    elif action_type == "collection":
        food.collections += 1
        food.save()
    elif action_type == "uncollection":
        food.collections -= 1
        food.save()
    else:
        pass

    return JsonResponse({
        'result': 'success',
    })