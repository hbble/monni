from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
	path('', views.index, name='index'),
	path('newinc/', views.AddIncomeView, name='AddIncome'),
	path('newexp/', views.AddExpenseView, name='AddExpense'),
	path('newexp/', views.postExp, name='submitExp'),
]