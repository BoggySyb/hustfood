from django.http import JsonResponse

def first_try(request):
    return JsonResponse({
        'result': "success",
        'data': "hello world",
    })