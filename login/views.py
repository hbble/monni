from django.shortcuts import render

def login(request):
	return render(request, 'login/login.html')

def signup(request):
	return render(request, 'login/register.html')

def forgot_pass(request):
	return render(request, 'login/forgot-password.html')