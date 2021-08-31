""""""
from django.contrib import admin
from django.urls import path
from rodneygram import views


urlpatterns = [
    path('hello-world/', views.hello_word),
    path('hi/', views.hi),
    path('admin/', admin.site.urls),
]
