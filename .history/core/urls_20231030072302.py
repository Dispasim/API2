
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('projet.urls', namespace='projet')),
    path('',include('projet_api.urls', namespace='projet_api'))
]
