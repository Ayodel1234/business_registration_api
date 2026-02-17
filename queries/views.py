from rest_framework import generics
from accounts.permissions import IsAdminUserRole
from .models import Query
from .serializers import QuerySerializer
from registrations.models import Registration
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status



class QueryCreateView(generics.CreateAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer
    permission_classes = [IsAdminUserRole]

    def perform_create(self, serializer):
        query = serializer.save()

        # When query is created, update registration status
        registration = query.registration
        registration.status = 'queried'
        registration.save()



class QueryRespondView(generics.UpdateAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        query = self.get_object()

        # Only owner of registration can respond
        if query.registration.user != request.user:
            return Response(
                {"detail": "Not allowed to respond to this query."},
                status=status.HTTP_403_FORBIDDEN
            )

        query.response = request.data.get("response")
        query.status = "responded"

        # Update registration status too
        registration = query.registration
        registration.status = "responded"
        registration.save()

        query.save()

        serializer = self.get_serializer(query)
        return Response(serializer.data)
