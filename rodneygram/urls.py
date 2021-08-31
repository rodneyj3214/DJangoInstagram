""""""
from django.contrib import admin
from django.urls import path
from rodneygram import views as local_views
from posts import views as posts_views

urlpatterns = [
    path('hello-world/', local_views.hello_word),
    path('hi/', local_views.hi),
    path('admin/', admin.site.urls),
    path('posts/', posts_views.list_post),
]
