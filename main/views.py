from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return render(request, 'main/base.html')

def AddIncome(request):
	pass

def AddExpense(request):
	pass
