from .views import index, ContactFormView
from django.urls import path

urlpatterns = [
    path('', index.as_view(), name='index'), 
    path('contact/', ContactFormView.as_view(), name='contact_form'
    ),
]