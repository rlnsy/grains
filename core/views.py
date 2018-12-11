from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Project

def index(request):
	project_list = Project.objects.order_by('-init_date')[:10]	# top 10
	template = loader.get_template('core/index.html')
	context = {
		'project_list': project_list,
	}
	return HttpResponse(template.render(context, request))

def project_detail(request, project_id):
	p = get_object_or_404(Project, pk=project_id)
	return render(request, 'core/project-details.html', {'project': p})