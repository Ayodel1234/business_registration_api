from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import PermissionDenied
from .models import Document
from .serializers import DocumentSerializer


# ===============================
# Upload Document (POST)
# ===============================
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

        # ===============================
        # Normal User Logic
        # ===============================
        if not user.is_staff:  # Better than user.role
            if registration.user != user:
                raise PermissionDenied("You cannot upload to this registration.")

            if document_type not in user_allowed:
                raise PermissionDenied("You are not allowed to upload this document type.")

        # ===============================
        # Admin Logic
        # ===============================
        else:
            if document_type not in admin_allowed:
                raise PermissionDenied("Admin cannot upload this document type.")

            if registration.status not in ['approved', 'completed', 'in_progress']:
                raise PermissionDenied(
                    "Cannot upload official documents unless registration is approved."
                )

        serializer.save(uploaded_by=user)


# ===============================
# List Documents (GET)
# ===============================
class DocumentListView(generics.ListAPIView):
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Document.objects.all()

        return Document.objects.filter(registration__user=user)