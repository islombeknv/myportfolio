from modeltranslation.translator import register, TranslationOptions

from posts.models import BlogModel


@register(BlogModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'long_description')

