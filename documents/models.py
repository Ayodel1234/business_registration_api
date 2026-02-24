from django.db import models
from django.conf import settings
from registrations.models import Registration


class Document(models.Model):
    DOCUMENT_TYPES = (
        ('certificate', 'CAC Certificate'),
        ('status_report', 'Status Report'),
        ('memart', 'MEMART'),
        ('name_approval', 'Name Approval Document'),
        ('supporting_doc', 'Supporting Document'),
        ('correction_doc', 'Correction Document'),
    )

    registration = models.ForeignKey(
        Registration,
        on_delete=models.CASCADE,
        related_name='documents'
    )

    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='uploaded_documents'
    )

    document_type = models.CharField(
        max_length=50,
        choices=DOCUMENT_TYPES
    )

    file = models.FileField(upload_to='registration_documents/')

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_document_type_display()} | RegID:{self.registration.id}"