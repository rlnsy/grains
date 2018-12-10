from django.shortcuts import render

def index(request):
	return HttpResponse("Core App Index")