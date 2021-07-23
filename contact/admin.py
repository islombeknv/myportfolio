from django.contrib import admin

from contact.models import ContactModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    search_fields = ['name', 'phone']
    list_display = ['name', 'phone', 'email']
    list_filter = ['created_at']
