from django.db import models
from django.conf import settings
from registrations.models import Registration


class Query(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('responded', 'Responded'),
        ('resolved', 'Resolved'),
    )

    registration = models.ForeignKey(
        Registration,
        on_delete=models.CASCADE,
        related_name='queries'
    )

    reason = models.TextField()
    instruction = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='open'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Query for {self.registration.id}"
