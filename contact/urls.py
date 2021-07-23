from django.urls import path

from contact.views import ContactCreateView, contact_send

app_name = 'contact'
urlpatterns = [
    path('', ContactCreateView.as_view(), name='create'),
    path('done/', contact_send),

]