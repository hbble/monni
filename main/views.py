from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return render(request, 'main/index.html')

def AddIncome(request):
	return render(request, 'main/income-form.html')

def AddExpense(request):
	return render(request, 'main/expense-form.html')
