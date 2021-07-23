from django.urls import path

from myportfolio.views import PortfoliolistView

app_name = 'portfolio'

urlpatterns = [
    path('', PortfoliolistView.as_view(), name='list'),
]
