from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("app.urls")),
    path("token/", include("token_auth.urls")),
    path("celery/", include("send_email_celery.urls")),
]
