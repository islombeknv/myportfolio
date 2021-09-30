from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
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

    def form_valid(self, form):
        obj = form.save()
        text = f'Name: {obj.name}\nEmail: {obj.email}\nPhone: {obj.phone}\nMessage: {obj.message}\nDate{obj.created_at}'
        send_mail(
            'Notification',
            text,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
        )
        return redirect(self.success_url)


def contact_send(request):
    messages.add_message(request, messages.INFO, 'Your message has been sent successfully')
    return redirect(reverse('pages:home'))
