from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('1.0.0/', include([
            path('auth/', include('apps.accounts.api.urls')),
        ])),
    ])),
]
