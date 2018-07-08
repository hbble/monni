from modeltranslation.translator import translator, TranslationOptions
from main.models import InCategory, OutCategory

class InCatTranslationOptions(TranslationOptions):
    '''Fields to translate for InCategory'''
    fields = ('name',)

class OutCatTranslationOptions(TranslationOptions):
    '''Fields to translate for OutCategory'''
    fields = ('name',)

translator.register(InCategory, InCatTranslationOptions)
translator.register(OutCategory, OutCatTranslationOptions)
