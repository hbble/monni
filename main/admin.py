from django.contrib import admin
from .models import InCategory, OutCategory, Income, Expense
from modeltranslation.admin import TranslationAdmin

class InCategoryAdmin(TranslationAdmin):
    pass

class OutCategoryAdmin(TranslationAdmin):
    pass

admin.site.register(InCategory, InCategoryAdmin)
admin.site.register(OutCategory, OutCategoryAdmin)

#temp
admin.site.register(Income)
admin.site.register(Expense)

