""""""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def hello_word(request):
    return HttpResponse('Hello, world')


urlpatterns = [
    path('hello-world/', hello_word),
    path('admin/', admin.site.urls),
]
