from django.urls import path
from .views import RegistrationListCreateView, RegistrationStatusUpdateView

urlpatterns = [
    path('', RegistrationListCreateView.as_view(), name='registration-list-create'),
    path('<int:id>/status/', RegistrationStatusUpdateView.as_view(), name='registration-status-update'),
]
