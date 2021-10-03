from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include(('dashboard.urls', 'dashboard'), namespace='dashboard')),
    path('resource/', include(('user_resource.urls', 'user_resource'), namespace='user_resource')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
