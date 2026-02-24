from django.urls import path
from .views import (
    RegistrationListCreateView,
    RegistrationStatusUpdateView,
    RegistrationApproveView,
)

urlpatterns = [
    path('', RegistrationListCreateView.as_view(), name='registration-list-create'),
    path('<int:id>/status/', RegistrationStatusUpdateView.as_view(), name='registration-status-update'),
    path('<int:id>/approve/', RegistrationApproveView.as_view(), name='registration-approve'),
]