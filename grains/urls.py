from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [

    path('', views.index),
    path('core/', include('core.urls')),
    path('admin/', admin.site.urls),

    # ACCOUNTS
    path('accounts/login/', views.login_form, name="user_login_form"),
    path('accounts/login/redirect/', views.user_login, name="user_login"),
    path('accounts/logout/', views.user_logout, name="user_logout"),
    path('accounts/new/redirect/', views.user_create, name='user_create'),
    path('accounts/new/', views.user_form, name='user_creation_form'),

]
