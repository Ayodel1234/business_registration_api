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

        # Base queryset depending on role
        if user.role == 'admin':
            queryset = Registration.objects.all()
        else:
            queryset = Registration.objects.filter(user=user)

        # 🔥 Add Status Filtering
        status_filter = self.request.query_params.get('status')
        if status_filter:
            queryset = queryset.filter(status=status_filter)

        return queryset

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
        registration.status = 'name_approved'
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
# Admin Raises Query
# ======================================
class RegistrationQueryView(UpdateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        registration = self.get_object()

        query_message = request.data.get('query_message')

        if not query_message:
            return Response(
                {"error": "query_message is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        registration.query_message = query_message
        registration.status = 'queried'
        registration.save()

        return Response(
            {"message": "Query sent to user successfully"},
            status=status.HTTP_200_OK
        )


# ======================================
# User Responds To Query
# ======================================
class RegistrationRespondView(UpdateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        registration = self.get_object()

        if registration.user != request.user:
            return Response(
                {"error": "You are not allowed to respond to this registration"},
                status=status.HTTP_403_FORBIDDEN
            )

        response_message = request.data.get('response_message')

        if not response_message:
            return Response(
                {"error": "response_message is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        registration.query_message = response_message
        registration.status = 'responded'
        registration.save()

        return Response(
            {"message": "Response submitted successfully"},
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

        status_counts = (
            Registration.objects
            .values('status')
            .annotate(count=Count('status'))
        )

        response_data = {
            "total_registrations": total
        }

        for item in status_counts:
            response_data[item['status']] = item['count']

        return Response(response_data)