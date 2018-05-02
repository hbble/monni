from django.urls import path

from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

app_name = 'auth'
urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'login/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'auth:login'}, name='logout'),
    
    # path('login', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('forgot/', views.forgot_pass, name='forgot_pass'),
]