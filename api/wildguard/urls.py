# wildguard/urls.py
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from apps.my_app.views import home_view
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.my_app.urls')),
    path('', home_view),
    path('upload/', views.upload_image, name='upload_image'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
