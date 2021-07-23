from django.urls import path

from posts.views import BlogView, BlogDetailView, CommetCreateView

app_name = 'blog'
urlpatterns = [
    path('', BlogView.as_view(), name='list'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('<int:pk>/comment/', CommetCreateView.as_view(), name='comment'),
]
