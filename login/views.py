from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def login(request):#not working
	if not request.user.is_authenticated:
		return render(request, 'login/login.html')
	else:
		return HttpResponseRedirect(reverse('main:index'))
		

def signup(request):
	return render(request, 'login/register.html')

def forgot_pass(request):
	return render(request, 'login/forgot-password.html')
