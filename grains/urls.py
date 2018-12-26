from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    # TODO: add an empty path
    path('', views.index),
    path('core/', include('core.urls')),
    path('admin/', admin.site.urls),
]
