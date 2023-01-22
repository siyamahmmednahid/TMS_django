from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('api/auth/', include('AuthenticationApp.urls')),
    path('api/home/', include('HomeApp.urls')),
    path('api/chat/', include('ChatApp.urls')),
    path('api/email/', include('EmailApp.urls')),
    path('api/event/', include('EventApp.urls')),
    path('api/todo/', include('TodoApp.urls')),
    path('api/users/', include('UserApp.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)