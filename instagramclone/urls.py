"""Modulo URL del instagramclone"""

# Django
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

# local
from instagramclone import views as local_views
from posts import views as posts_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello-world/', local_views.hello_world),
    path('sort/', local_views.sort_integers),
    path('hi/<str:name>/<int:age>/', local_views.hi),

    path('posts/', posts_views.list_posts)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
