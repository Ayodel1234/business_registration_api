from django.db import models
from django.conf import settings


class Registration(models.Model):
    SERVICE_CHOICES = (
        ('business_name', 'Business Name'),
        ('ltd', 'Private Limited Company'),
    )

    STATUS_CHOICES = (
        ('submitted', 'Submitted'),
        ('queried', 'Queried'),
        ('responded', 'User Responded'),
        ('name_approved', 'Name Approved'),
        ('name_denied', 'Name Denied'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('rejected', 'Rejected'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='registrations'
    )

    service_type = models.CharField(
        max_length=20,
        choices=SERVICE_CHOICES
    )

    name_option_1 = models.CharField(max_length=255)
    name_option_2 = models.CharField(max_length=255)

    approved_name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    rejection_reason = models.TextField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='submitted'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ID:{self.id} | {self.name_option_1} | {self.user.email}"