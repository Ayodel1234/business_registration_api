from rest_framework import serializers
from .models import Registration


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = [
            'id',
            'service_type',
            'name_option_1',
            'name_option_2',
            'approved_name',
            'status',
            'created_at',
        ]
        read_only_fields = ['approved_name', 'status', 'created_at']

class RegistrationMiniSerializer(serializers.ModelSerializer):
    owner_email = serializers.EmailField(source='user.email')

    class Meta:
        model = Registration
        fields = [
            'id',
            'service_type',
            'name_option_1',
            'name_option_2',
            'status',
            'owner_email',
        ]
