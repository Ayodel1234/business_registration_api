from rest_framework import generics, permissions
from .models import Registration
from .serializers import RegistrationSerializer


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
