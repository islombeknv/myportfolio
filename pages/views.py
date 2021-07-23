from django.shortcuts import render
from django.views.generic import TemplateView

from posts.models import BlogModel, OurClientsModel, OurPartnersmodel


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = BlogModel.objects.order_by('-pk')[:3]
        context['clients'] = OurClientsModel.objects.order_by('-pk')[:3]
        context['partners'] = OurPartnersmodel.objects.order_by('-pk')[:6]
        return context
