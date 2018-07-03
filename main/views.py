from datetime import timedelta
from itertools import chain
from operator import attrgetter
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render

from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _

from .models import InCategory, OutCategory, Income, Expense
from .stat import StatsData

@login_required
def index(request):
    inc_list = Income.objects.filter(
        user=request.user
        ).order_by('-date')

    exp_list = Expense.objects.filter(
        user=request.user
        ).order_by('-date')

    #error empty list
    if not inc_list or not exp_list:
        return render(request, 'main/index.html', {'error_empty': _('Nothing to show here.')})

    table_row_list = sorted(
        chain(inc_list, exp_list),
        key=attrgetter('date'),
        reverse=True)

    context = {
        'table_row_list': table_row_list,
    }
    return render(request, 'main/index.html', context)

@login_required
def cat_view(request):
    return render(request, 'main/categories.html')

@login_required
def add_income_view(request):
    cat_list = get_list_or_404(InCategory)
    latest_inc_list = Income.objects.filter(
        date__lte=timezone.now(),
        user=request.user
        ).order_by('-date')[:3]
    
    context = {
        'latest_inc_list': latest_inc_list,
        'cat_list': cat_list,
    }
    return render(request, 'main/income-form.html', context)

@login_required
def add_expense_view(request):
    cat_list = get_list_or_404(OutCategory)
    latest_exp_list = Expense.objects.filter(
        date__lte=timezone.now(),
        user=request.user
        ).order_by('-date')[:3]

    context = {
        'latest_exp_list': latest_exp_list,
        'cat_list': cat_list,
    }
    return render(request, 'main/expense-form.html', context)

def post_income(request):
    try:
        user = request.user
        category = InCategory.objects.get(pk=request.POST['category'])
        amount = request.POST.get('amount')
        date = timezone.now()

        income = Income(user=user, category=category, amount=amount, date=date)
        income.save()
    except:
        #Redisplay the form
        context = {
            'error_message': "An error occured. Try again.",
        }
        return render(request, 'main/income-form.html', context)
    else:
        return HttpResponseRedirect(reverse('main:addIncome'))

def post_expense(request):
    try:
        user = request.user
        category = OutCategory.objects.get(pk=request.POST['category'])
        amount = request.POST.get('amount')
        date = timezone.now()

        expense = Expense(user=user, category=category, amount=amount, date=date)
        expense.save()
    except:
        #Redisplay the form
        context = {
            'error_message': "An error occured.",
        }
        return render(request, 'main/expense-form.html', context)
    else:
        return HttpResponseRedirect(reverse('main:addExpense'))


def edit_expense(request, edit_id):
    try:
        expense = get_object_or_404(Expense, pk=edit_id)
        
        expense.category = OutCategory.objects.get(pk=request.POST['category'])
        expense.amount = request.POST.get('amount')
        expense.save()
    except:
        #Redisplay the form
        context = {
            'error_editing_message': "An error occured.",
        }
        return render(request, 'main/expense-form.html', context)
    else:
        return HttpResponseRedirect(reverse('main:addExpense'))

def edit_income(request, edit_id):
    try:
        income = get_object_or_404(Income, pk=edit_id)
        
        income.category = InCategory.objects.get(pk=request.POST['category'])
        income.amount = request.POST.get('amount')
        income.save()
    except:
        #Redisplay the form
        context = {
            'error_editing_message': "An error occured.",
        }
        return render(request, 'main/income-form.html', context)
    else:
        return HttpResponseRedirect(reverse('main:addIncome'))

def delete_expense(request, edit_id):
    try:
        expense = get_object_or_404(Expense, pk=edit_id)
        expense.delete()
    except:
        #Redisplay the form
        context = {
            'error_editing_message': "An error occured.",
        }
        return render(request, 'main/expense-form.html', context)
    else:
        return HttpResponseRedirect(reverse('main:addExpense'))

def delete_income(request, edit_id):
    try:
        income = get_object_or_404(Income, pk=edit_id)
        income.delete()
    except:
        #Redisplay the form
        context = {
            'error_editing_message': "An error occured.",
        }
        return render(request, 'main/income-form.html', context)
    else:
        return HttpResponseRedirect(reverse('main:addIncome'))

@login_required
def all_operations_view(request):
    #try-except needed
    latest_exp_list = Expense.objects.filter(
        user=request.user
        ).order_by('-date')

    latest_inc_list = Income.objects.filter(
        user=request.user
        ).order_by('-date')

    context = {
        'latest_exp_list': latest_exp_list,
        'latest_inc_list': latest_inc_list,
    }
    return render(request, 'main/all-operations.html', context)

@login_required
def stats_view(request):
    list_e = Expense.objects.filter(user=request.user)
    list_i = Income.objects.filter(user=request.user)

    #error empty list
    if not list_e or not list_i:
        return render(request, 'main/stats.html', {'error_empty': 'Nothing to show here.'})

    return render(request, 'main/stats.html')

@login_required
def get_data(request):
    '''Getting data for Charts'''
    provider = StatsData()

    data = {
        "pie_chart": provider.pie_exp_data(request),
        "line_chart": provider.line_data(request),
        "bar_chart": provider.bar_data(request),
    }

    return JsonResponse(data)