from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from rec_systems.models.appuser.appuser import AppUser

def register(request):
    data = request.GET
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()
    password_confirm = data.get("confirm_password", "").strip()
    if not username:
        return JsonResponse({
            'result': '用户名不能为空',
        })
    if not password:
        return JsonResponse({
            'result': '密码不能为空',
        })
    if password_confirm != password:
        return JsonResponse({
            'result': '两个密码不一致',
        })
    if User.objects.filter(username=username).exists():
        return JsonResponse({
            'result': '用户名已存在',
        })
    user = User(username=username)
    user.set_password(password)
    user.save()

    AppUser.objects.create(user=user, photo="http://img.520touxiang.com/uploads/allimg/171123/3-1G123211117.jpg")
    login(request, user)
    return JsonResponse({
        'result': 'success',
    })
