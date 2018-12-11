from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	# TODO: add an empty path
	path('core/', include('core.urls')),
    path('admin/', admin.site.urls),
]
