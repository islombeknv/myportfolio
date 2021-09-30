from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView

from contact.forms import ContactModelForm
from contact.models import ContactModel


class ContactCreateView(CreateView):
    template_name = 'index.html'
    model = ContactModel
    form_class = ContactModelForm
    success_url = '/'


