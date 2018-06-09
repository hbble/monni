from django.contrib import admin
from .models import InCategory, OutCategory, Income, Expense

admin.site.register(InCategory)
admin.site.register(OutCategory)

#temp
admin.site.register(Income)
admin.site.register(Expense)

