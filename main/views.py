from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import InCategory, OutCategory


def index(request):
	return render(request, 'main/index.html')

def AddIncomeView(request):
	cat_list = get_list_or_404(InCategory)
	context = {
		'cat_list': cat_list,
	}
	return render(request, 'main/income-form.html', context)

def AddExpenseView(request):
	cat_list = get_list_or_404(OutCategory)
	context = {
		'cat_list': cat_list,
	}
	return render(request, 'main/expense-form.html', context)

def postExp(request):
	pass
