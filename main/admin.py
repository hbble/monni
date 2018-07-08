from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import InCategory, OutCategory, Income, Expense

class InCategoryAdmin(TranslationAdmin):
    '''Allowing translate InCategory in admin panel'''
    pass

class OutCategoryAdmin(TranslationAdmin):
    '''Allowing translate OutCategory in admin panel'''
    pass

admin.site.register(InCategory, InCategoryAdmin)
admin.site.register(OutCategory, OutCategoryAdmin)

#temp
admin.site.register(Income)
admin.site.register(Expense)
