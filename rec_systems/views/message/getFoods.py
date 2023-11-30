from django.http import JsonResponse
from rec_systems.models.food.food import Food

def getFoods(request):
    event = request.GET.get('event')
    if event == "getStarFoods":
        return getStarFoods()
    elif event == "getOneFood":
        return getOneFood(request.GET.get('id'))

    return JsonResponse({
        'result': "fail",
    })

def foodData(food):
    return {
        'id': food.food_id,
        'name': food.name,
        'position': food.position,
        'price': food.price,
        'imgUrl': food.imgUrl,
        'class1': food.class1,
        'class2': food.class2,
        'likes': food.likes,
        'collections': food.collections,
    }

def getOneFood(id):
    food = Food.objects.all().get(food_id=id)
    return JsonResponse({
        'result': "success",
        'data': foodData(food),
    })

def getStarFoods():
    foods = []
    for i in range(1, 5):
        food = Food.objects.all().get(food_id = str(i))
        foods.append(foodData(food))

    return JsonResponse({
        'result': "success",
        'foods': foods,
    })