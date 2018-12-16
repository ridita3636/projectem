from django.http import HttpResponse

def index(request):

    return HttpResponse("<h1>Hellow the world</h1>")