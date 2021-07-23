from django.urls import path

from pages.views import HomeTemplateView

app_name = 'pages'

urlpatterns =[
    path('', HomeTemplateView.as_view(), name='home')
]