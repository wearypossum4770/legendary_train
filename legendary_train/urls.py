from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

from users.views import commander

urlpatterns = [
    path("commander/", commander),
    path("leads/", include("leads.urls")),
    path("blog/", include("blog.urls")),
    path("users/", include("users.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("chat/", include("chat.urls")),
    path("admin/", admin.site.urls),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
