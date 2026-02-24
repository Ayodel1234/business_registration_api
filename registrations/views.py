from rest_framework import generics, permissions
from .models import Registration
from .serializers import RegistrationSerializer
from rest_framework import generics
from accounts.permissions import IsAdminUserRole

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from accounts.permissions import IsAdminRole


from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated



class RegistrationListCreateView(generics.ListCreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # Admin can see all registrations
        if user.role == 'admin':
            return Registration.objects.all()

        # Normal users see only their own
        return Registration.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RegistrationStatusUpdateView(generics.UpdateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAdminUserRole]
    lookup_field = 'id'



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
        registration.status = 'approved'
        registration.save()

        return Response(
            {"message": "Registration approved successfully"},
            status=status.HTTP_200_OK
        )