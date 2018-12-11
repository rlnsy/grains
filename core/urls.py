from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [

	# ex: /core/
	path('', views.index, name="index_default"),	# same as projects root

	# ex: /core/projects
	path('projects', views.index, name="index"),	# projects list

	# ex: /core/projects/22
	path('projects/<int:project_id>/', views.project_detail, name='project_details')
]