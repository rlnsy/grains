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
        'authed': False,
        'user': '',
    }

    if request.user.is_authenticated:
        context['authed'] = True,
        context['user'] = request.user.username

    return HttpResponse(template.render(context, request))

def index_redirect(request):
    return HttpResponseRedirect(reverse('core:index', args=()))

def project_detail(request, project_id):
    p = get_object_or_404(Project, pk=project_id)
    return render(request, 'core/project-details.html', {'project': p})

def project_form(request):
    template = loader.get_template('core/submit.html')
    context = {}
    return HttpResponse(template.render(context, request))

from django.utils import timezone

def project_create(request):
    descriptor = request.POST['descriptor']
    tag = "new"
    current_date = timezone.now()
    p = Project(descriptor=descriptor, project_tag=tag, init_date=current_date)
    p.save()
    return HttpResponseRedirect(reverse('core:project_details', args=(p.id,)))

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def login_form(request):
    template = loader.get_template('core/login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def user_login(request):
    uname = request.POST['username']
    pwd = request.POST['password']
    user = authenticate(request, username=uname, password=pwd)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('core:index', args=()))
    else:
        return HttpResponse("invalid login")

def user_logout(request):
    logout(request)
    return HttpResponse("successfully logged out")

def user_form(request):
    template = loader.get_template('core/newuser.html')
    context = {}
    return HttpResponse(template.render(context, request))

def user_create(request):
    uname = request.POST['username']
    pwd = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_user(uname, email, pwd)
    user.save()
    return HttpResponse("user created")

