from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [

    # CORE PATH
    # ex: /core/
    path('', views.index_redirect, name="index_default"),  # needless redirect

    # PROJECTS
    path('projects/', views.index, name="index"),	# projects list
    path('projects/<int:project_id>/', views.project_detail, name='project_details'),
    path('projects/submit/', views.project_create, name="project_create"),  # recieves POST info
    path('projects/submit/form/', views.project_form, name='project_submission_form'),

    # USER PAGES
    path('users/<str:username>/', views.user_detail, name='user_details'),
]