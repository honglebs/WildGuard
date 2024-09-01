# wildguard/urls.py

from django.contrib import admin
from django.urls import path, include
from apps.my_app.views import home_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.my_app.urls')),
    path('', home_view)

]
