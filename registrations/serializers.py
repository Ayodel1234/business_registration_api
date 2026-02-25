from rest_framework import serializers
from .models import Registration
from documents.serializers import DocumentSerializer



class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'
        read_only_fields = ['user', 'status', 'approved_name', 'rejection_reason', 'created_at']

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)
    

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
