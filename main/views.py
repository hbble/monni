from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import InCategory, OutCategory, Incomes, Expenses
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def index(request):
	return render(request, 'main/index.html')

@login_required
def AddIncomeView(request):
	cat_list = get_list_or_404(InCategory)
	latest_inc_list = Incomes.objects.filter(
		date__lte=timezone.now(),
		user=request.user
		).order_by('-date')[:3]
	
	context = {
		'latest_inc_list': latest_inc_list,
		'cat_list': cat_list,
	}
	return render(request, 'main/income-form.html', context)

@login_required
def AddExpenseView(request):
	cat_list = get_list_or_404(OutCategory)
	latest_exp_list = Expenses.objects.filter(
		date__lte=timezone.now(),
		user=request.user
		).order_by('-date')[:3]

	context = {
		'latest_exp_list': latest_exp_list,
		'cat_list': cat_list,
	}
	return render(request, 'main/expense-form.html', context)

def PostIncome(request):
	try:
		user = request.user
		category = InCategory.objects.get(pk=request.POST['category'])
		amount = request.POST.get('amount')

		income = Incomes(user=user, category=category, amount=amount)
		income.save()
	except:
		#Redisplay the form
		context = {
			'error_message': "An error occured. Try again.",
		}
		return render(request, 'main/income-form.html', context)
	else:
		return HttpResponseRedirect(reverse('main:AddIncome'))

def PostExpense(request):
	try:
		user = request.user
		category = OutCategory.objects.get(pk=request.POST['category'])
		amount = request.POST.get('amount')

		expense = Expenses(user=user, category=category, amount=amount)
		expense.save()
	except:
		#Redisplay the form
		context = {
			'error_message': "An error occured.",
		}
		return render(request, 'main/expense-form.html', context)
	else:
		return HttpResponseRedirect(reverse('main:AddExpense'))
