from django.http import JsonResponse
from rec_systems.models.food.food import Food

def getFoods(request):
    event = request.GET.get('event')
    if event == "getStarFoods":
        return getStarFoods()

    return JsonResponse({
        'result': "fail",
    })

def foodData(food):
    return {
        'name': food.name,
        'position': food.position,
        'price': food.price,
        'imgUrl': food.imgUrl,
    }

def getStarFoods():
    foods = []
    for i in range(1, 5):
        food = Food.objects.all().get(food_id = str(i))
        foods.append(foodData(food))

    return JsonResponse({
        'result': "success",
        'foods': foods,
    })