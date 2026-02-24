from django.urls import path
from .views import (
    RegistrationListCreateView,
    RegistrationStatusUpdateView,
    RegistrationApproveView,
    RegistrationRejectView,
    RegistrationDetailView,
    AdminDashboardView,
)

urlpatterns = [
    path('admin/dashboard/', AdminDashboardView.as_view(), name='admin-dashboard'),
    path('', RegistrationListCreateView.as_view(), name='registration-list-create'),
    path('<int:id>/status/', RegistrationStatusUpdateView.as_view(), name='registration-status-update'),
    path('<int:id>/', RegistrationDetailView.as_view(), name='registration-detail'),
    path('<int:id>/approve/', RegistrationApproveView.as_view(), name='registration-approve'),
    path('<int:id>/reject/', RegistrationRejectView.as_view(), name='registration-reject'),
]       