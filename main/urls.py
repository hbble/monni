from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('newinc/', views.add_income_view, name='addIncome'),
    path('newexp/', views.add_expense_view, name='addExpense'),
    path('newexp/submit', views.post_expense, name='submitExp'),
    path('newinc/submit', views.post_income, name='submitInc'),
    path('newexp/<int:edit_id>/edit', views.edit_expense, name='editExpense'),
    path('newinc/<int:edit_id>/edit', views.edit_income, name='editIncome'),
    path('all/', views.all_operations_view, name='allOperations'),
    path('stats/', views.stats_view, name='stats'),
    path('stats/data/', views.get_data, name='statsData'),
    path('cat/', views.cat_view, name='categories'),
    

]