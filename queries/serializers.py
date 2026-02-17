from rest_framework import serializers
from .models import Query
from registrations.serializers import RegistrationMiniSerializer


class QuerySerializer(serializers.ModelSerializer):
    registration_details = RegistrationMiniSerializer(
        source='registration',
        read_only=True
    )

    class Meta:
        model = Query
        fields = [
            'id',
            'registration',          # used for POST
            'registration_details',  # used for display
            'reason',
            'instruction',
            'response',
            'status',
            'created_at',
        ]
        read_only_fields = ['status', 'created_at']
