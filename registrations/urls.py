from django.urls import path
from .views import RegistrationListCreateView

urlpatterns = [
    path('', RegistrationListCreateView.as_view(), name='registration-list-create'),
]
