from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('product.urls')),
    path('admin/', admin.site.urls),
    # path('auth/', include('django.contrib.auth.urls')),
]


urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)