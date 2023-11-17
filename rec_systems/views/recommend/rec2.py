from django.http import JsonResponse
from rec_systems.models.food.food import Food

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
        food = Food.objects.all().get(food_id="1")
        return JsonResponse({
            'result': "success",
            'data': foodData(food),
        })
    else:
        return JsonResponse({
            'result': "fail",
        })