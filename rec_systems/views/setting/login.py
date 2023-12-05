from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from rec_systems.models.appuser.appuser import AppUser
from datetime import datetime, timedelta
import pytz

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

    # 检查是否注册已一周，更新为老用户
    appuser = AppUser.objects.all().get(user=user)
    if appuser.is_new_user:
        wall = datetime.now() - timedelta(days=7)
        wall = wall.replace(tzinfo=pytz.timezone('Asia/Shanghai'))
        if appuser.created_time < wall:
            appuser.is_new_user = False
            appuser.save()

    return JsonResponse({
        'result': 'success',
    })