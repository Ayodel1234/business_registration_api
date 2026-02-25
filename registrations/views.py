from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count

from .models import Registration
from .serializers import RegistrationSerializer
from accounts.permissions import IsAdminUserRole, IsAdminRole


# ======================================
# List & Create Registrations
# ======================================
class RegistrationListCreateView(generics.ListCreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # Admin sees all
        if user.role == 'admin':
            return Registration.objects.all()

        # Normal user sees only their own
        return Registration.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ======================================
# Update Status (Generic Admin Update)
# ======================================
class RegistrationStatusUpdateView(generics.UpdateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAdminUserRole]
    lookup_field = 'id'


# ======================================
# Approve Registration
# ======================================
class RegistrationApproveView(UpdateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        registration = self.get_object()

        approved_name = request.data.get('approved_name')

        if not approved_name:
            return Response(
                {"error": "approved_name is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        registration.approved_name = approved_name
        registration.status = 'name_approved'   # ✅ FIXED HERE
        registration.save()

        return Response(
            {"message": "Registration approved successfully"},
            status=status.HTTP_200_OK
        )


# ======================================
# Reject Registration
# ======================================
class RegistrationRejectView(UpdateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        registration = self.get_object()

        rejection_reason = request.data.get('rejection_reason')

        if not rejection_reason:
            return Response(
                {"error": "rejection_reason is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        registration.status = 'rejected'
        registration.rejection_reason = rejection_reason
        registration.approved_name = None
        registration.save()

        return Response(
            {"message": "Registration rejected successfully"},
            status=status.HTTP_200_OK
        )


# ======================================
# Retrieve Single Registration
# ======================================
class RegistrationDetailView(RetrieveAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user

        if user.role == 'admin':
            return Registration.objects.all()

        return Registration.objects.filter(user=user)


# ======================================
# Admin Dashboard Stats
# ======================================
class AdminDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsAdminRole]

    def get(self, request):
        total = Registration.objects.count()

        status_counts = Registration.objects.values('status') \
            .annotate(count=Count('status'))

        response_data = {
            "total_registrations": total
        }

        for item in status_counts:
            response_data[item['status']] = item['count']

        return Response(response_data)