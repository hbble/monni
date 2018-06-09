from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import views as auth_views

# def login(request, *args, **kwargs):
# 	if request.method == 'POST':
# 		if not request.POST.get('remember_me', None):
# 			request.session.set_expiry(0)#not working
    
# 	return auth_views.login(request, *args, **kwargs)
		

def signup(request):
	return render(request, 'login/register.html')

def forgot_pass(request):
	return render(request, 'login/forgot-password.html')
