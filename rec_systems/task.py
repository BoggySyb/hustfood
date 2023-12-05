from django.core.cache import cache
def UserCF():
    pass

def generate_recommendation():
    cache.set("hello", "world")