from django.contrib import admin
from django.urls import path
import MyAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/',MyAPI),
]
