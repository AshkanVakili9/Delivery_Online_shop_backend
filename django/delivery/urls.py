from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('user/', include('user.urls')),
    path('product/', include('product.urls')),
    path('history/', include('history.urls')),
    path('cart/', include('cart.urls')),
    # path('chat/', include('chat.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
