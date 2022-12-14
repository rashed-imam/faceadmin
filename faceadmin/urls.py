from django.urls import path, include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('face.urls')),
    path('api-auth/', include('rest_framework.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)