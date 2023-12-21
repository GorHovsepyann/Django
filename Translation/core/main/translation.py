from .models import product
from modeltranslation.translator import register, TranslationOptions

@register(product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'about',)