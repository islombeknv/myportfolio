from django.views.generic import ListView

from myportfolio.models import PortfolioModel, CategoryModel


class PortfoliolistView(ListView):
    template_name = 'my_works.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        return context

    def get_queryset(self):
        qs = PortfolioModel.objects.order_by('-pk')
        cat = self.request.GET.get('cat')
        if cat:
            return qs.filter(category_id=cat)
        return qs
