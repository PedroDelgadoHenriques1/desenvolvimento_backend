from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("usipav/", include("usipav.urls")),
    path("admin/", admin.site.urls),
]
