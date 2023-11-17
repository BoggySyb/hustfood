from django.http import JsonResponse
from rec_systems.models.store.store import Store

def getStores(request):
    event = request.GET.get('event')
    if event == "getStoreList":
        return getStoreList()

def storeData(store):
    return {
        'name': store.name,
        'starS': int(store.stars),
        'openTime': store.open_time,
        'imageList': [store.img1, store.img2, store.img3],
    }

def getStoreList():
    storeList = []
    for i in range(4):
        store = Store.objects.all().get(store_id = str(i))
        storeList.append(storeData(store))
    return JsonResponse({
        'result': "success",
        'storeList': storeList,
    })