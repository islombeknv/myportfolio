from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from posts.forms import CommentForm
from posts.models import BlogModel


class BlogView(ListView):
    template_name = 'blog.html'
    paginate_by = 3

    def get_queryset(self):
        qs = BlogModel.objects.order_by('-pk')
        tag = self.request.GET.get('tag')
        if tag:
            return qs.filter(Q(tags__title=tag))
        return qs


class BlogDetailView(DetailView):
    model = BlogModel
    template_name = 'blog-details.html'


class CommetCreateView(CreateView):
    template_name = 'blog-details.html'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post = get_object_or_404(BlogModel, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail', kwargs={'pk': self.kwargs.get('pk')})
