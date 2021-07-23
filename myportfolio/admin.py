from django.contrib import admin

from myportfolio.models import PortfolioModel, CategoryModel


@admin.register(PortfolioModel)
class PortfolioModelAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'created_at']
    list_filter = ['created_at']


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
