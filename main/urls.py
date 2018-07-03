from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('newinc/', views.add_income_view, name='addIncome'),
    path('newexp/', views.add_expense_view, name='addExpense'),
    path('newexp/submit', views.post_expense, name='submitExp'),
    path('newinc/submit', views.post_income, name='submitInc'),
    path('newexp/<int:edit_id>/edit', views.edit_expense, name='editExpense'),
    path('newexp/<int:edit_id>/delete', views.delete_expense, name='deleteExpense'),
    path('newinc/<int:edit_id>/edit', views.edit_income, name='editIncome'),
    path('newinc/<int:edit_id>/delete', views.delete_income, name='deleteIncome'),
    path('all/', views.all_operations_view, name='allOperations'),
    path('stats/', views.stats_view, name='stats'),
    path('stats/data/', views.get_data, name='statsData'),
    path('cat/', views.cat_view, name='categories'),
]