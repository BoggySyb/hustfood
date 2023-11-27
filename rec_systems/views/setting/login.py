from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from rec_systems.models.appuser.appuser import AppUser

def signin(request):
    data = request.GET
    username = data.get('username')
    password = data.get('password')
    user = authenticate(username=username, password=password)
    if not user:
        return JsonResponse({
            'result': '用户名密码不正确',
        })
    login(request, user)
    appuser = AppUser.objects.all().get(user=user)
    return JsonResponse({
        'result': 'success',
        'username': appuser.user.username,
        'userimg': appuser.photo,
    })