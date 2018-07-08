from django.shortcuts import render

def signup(request):
    '''Signup view'''
    return render(request, 'login/register.html')

def forgot_pass(request):
    '''Forgot password view'''
    return render(request, 'login/forgot-password.html')
