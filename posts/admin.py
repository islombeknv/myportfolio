from django.contrib import admin

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
class BlogModelAdmin(admin.ModelAdmin):
    list_filter = ['created_at', ]
    list_display = ['title', 'created_at']
    search_fields = ['title', ]
    autocomplete_fields = ['tags', 'category']


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
