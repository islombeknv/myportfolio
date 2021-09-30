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
    success_url = '/contact/done/'


def contact_send(request):
    messages.add_message(request, messages.INFO, 'Your message has been sent successfully')
    return redirect(reverse('pages:home'))
