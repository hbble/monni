from modeltranslation.translator import translator, TranslationOptions
from main.models import InCategory, OutCategory, Income, Expense

class InCatTranslationOptions(TranslationOptions):
    fields = ('name',)

class OutCatTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(InCategory, InCatTranslationOptions)
translator.register(OutCategory, OutCatTranslationOptions)
