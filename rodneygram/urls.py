""""""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

from posts import views as posts_views
from rodneygram import views as local_views

urlpatterns = [
                  path('hello-world/', local_views.hello_word),
                  path('hi/', local_views.hi),
                  path('admin/', admin.site.urls),
                  path('posts/', posts_views.list_post),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
