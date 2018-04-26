from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
	path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('forgot/', views.forgot_pass, name='forgot_pass'),
]