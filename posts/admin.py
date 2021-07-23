from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from posts.models import BlogModel, OurClientsModel, OurPartnersmodel, TagBlogModel, CategoryBlogModel, CommentModel


@admin.register(TagBlogModel)
class TagModelAdmin(admin.ModelAdmin):
    list_filter = ['created_at', ]
    list_display = ['title', 'created_at']
    search_fields = ['title', ]


@admin.register(CategoryBlogModel)
class CategoryBlogModelAdmin(admin.ModelAdmin):
    list_filter = ['created_at', ]
    list_display = ['title', 'created_at']
    search_fields = ['title', ]


@admin.register(BlogModel)
class BlogModelAdmin(TranslationAdmin):
    list_filter = ['created_at', ]
    list_display = ['title', 'created_at']
    search_fields = ['title', ]
    autocomplete_fields = ['tags', 'category']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(OurClientsModel)
class OurClientsModelAdmin(admin.ModelAdmin):
    list_filter = ['created_at']
    list_display = ['name', 'position', 'created_at']
    search_fields = ['name']


@admin.register(OurPartnersmodel)
class OurPartnersmodelAdmin(admin.ModelAdmin):
    list_filter = ['created_at']
    list_display = ['title', 'created_at']
    search_fields = ['title']


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'created_on']
    list_filter = ['created_on']
    search_fields = ['name', 'email']
