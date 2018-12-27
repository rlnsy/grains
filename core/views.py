from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Project, UserProxy
from .utils import auth_context


def index(request):
    project_list = Project.objects.order_by('-init_date')[:10]	# top 10
    template = loader.get_template('core/index.html')
    context = auth_context(request)
    context['project_list'] = project_list
    return HttpResponse(template.render(context, request))


def index_redirect(request):
    return HttpResponseRedirect(reverse('core:index', args=()))


def project_detail(request, project_id):
    p = get_object_or_404(Project, pk=project_id)
    return render(request, 'core/project-details.html', {'project': p})


@login_required
def project_form(request):
    template = loader.get_template('core/submit.html')
    context = {}
    return HttpResponse(template.render(context, request))


@login_required
def project_create(request):
    descriptor = request.POST['descriptor']
    tag = "new"
    current_date = timezone.now()
    p = Project(descriptor=descriptor, project_tag=tag,
                init_date=current_date, creator=request.user)
    p.save()
    return HttpResponseRedirect(reverse('core:project_details', args=(p.id,)))


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


def user_detail(request, username):
    context = auth_context(request)
    try:
        u = UserProxy.objects.get(username=username)
        projects = u.get_projects()
        context['username'] = username
        context['project_list'] = projects
    except User.DoesNotExist:
        raise Http404("User does not exist")

    template = loader.get_template('core/user_profile.html')
    return HttpResponse(template.render(context, request))
