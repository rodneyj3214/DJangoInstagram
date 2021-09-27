""""""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from posts import views as posts_views
from rodneygram import views as local_views
from users import views as users_views

urlpatterns = [
                  path('hello-world/', local_views.hello_word, name='hello_world'),
                  path('hi/', local_views.hi),
                  path('admin/', admin.site.urls),
                  path('', posts_views.list_post, name='feed'),
                  path('posts/new/', posts_views.create_post, name='create_post'),
                  path('users/login/', users_views.login_view, name='login'),
                  path('users/logout/', users_views.logout_view, name='logout'),
                  path('users/signup/', users_views.signup_view, name='signup'),
                  path('users/me/profile/', users_views.update_profile, name='update_profile'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
