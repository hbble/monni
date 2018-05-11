from django.contrib import admin
from .models import InCategory, OutCategory, Incomes, Expenses

admin.site.register(InCategory)
admin.site.register(OutCategory)

#temp
admin.site.register(Incomes)
admin.site.register(Expenses)

