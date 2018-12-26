from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [

    # CORE PATH
    # ex: /core/
    path('', views.index_redirect, name="index_default"),	# needless redirect

    # PROJECTS
    # ex: /core/projects
    path('projects', views.index, name="index"),	# projects list
    # ex: /core/projects/22
    path('projects/<int:project_id>/', views.project_detail, name='project_details'),
    path('projects/submit/', views.project_create, name="project_create"),	# recieves POST info
    path('projects/submit/form', views.project_form, name='project_submission_form'),

    # USERS
    path('login', views.login_form, name="user_login_form"),        # TODO: use auth views
    path('login/redirect', views.user_login, name="user_login"),
    path('logout', views.user_logout, name="user_logout"),
    path('users/new/redirect', views.user_create, name='user_create'),
    path('users/new', views.user_form, name='user_creation_form'),
    path('users/<str:username>/', views.user_detail, name='user_details'),

]