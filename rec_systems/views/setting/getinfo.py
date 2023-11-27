from django.http import JsonResponse
from rec_systems.models.appuser.appuser import AppUser

def getinfo_Web(request):
    user = request.user
    print(user)
    if not user.is_authenticated:
        return JsonResponse({
            'result': '未登录',
        })
    else:
        appuser = AppUser.objects.all().get(user=user)
        return JsonResponse({
            'result': 'success',
            'username': appuser.user.username,
            'userimg': appuser.photo,
        })

def getinfo(request):
    platform = request.GET.get('platform')
    if platform == 'app':
        return getinfo_Web(request)
    else:
        return JsonResponse({
            'result': '登录平台错误',
        })
