from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/', include('app.urls.api.v1')),
    path('admin/', admin.site.urls),
]
