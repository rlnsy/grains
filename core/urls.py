from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [

	# ex: /core/
	path('', views.index_redirect, name="index_default"),	# needless redirect

	# ex: /core/projects
	path('projects', views.index, name="index"),	# projects list

	# ex: /core/projects/22
	path('projects/<int:project_id>/', views.project_detail, name='project_details'),

	path('projects/submit/', views.project_create, name="project_create"),	# recieves POST info

	path('projects/submit/form', views.project_form, name='project_submission_form'),
]