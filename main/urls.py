from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('newinc/', views.AddIncome, name='AddIncome'),
	path('newexp/', views.AddExpense, name='AddExpense'),
]