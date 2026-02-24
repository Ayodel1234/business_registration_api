from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Document
from .serializers import DocumentSerializer
from rest_framework.exceptions import PermissionDenied


class DocumentUploadView(generics.CreateAPIView):
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        registration = serializer.validated_data['registration']
        document_type = serializer.validated_data['document_type']
        user = self.request.user

        user_allowed = ['supporting_doc', 'correction_doc']
        admin_allowed = ['certificate', 'status_report', 'memart', 'name_approval']

        # If normal user
        if not user.role == 'admin':
            if registration.user != user:
                raise PermissionDenied("You cannot upload to this registration.")

            if document_type not in user_allowed:
                raise PermissionDenied("You are not allowed to upload this document type.")

        # If admin
        else:
            if document_type not in admin_allowed:
                raise PermissionDenied("Admin cannot upload this document type.")

        serializer.save(uploaded_by=user)

class DocumentListView(generics.ListAPIView):
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'admin':
            return Document.objects.all()

        return Document.objects.filter(registration__user=user)