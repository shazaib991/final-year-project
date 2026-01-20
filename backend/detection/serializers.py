from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreateSerializer(BaseUserCreateSerializer):
    """
    Custom serializer that makes email optional and auto-generates it
    based on username if not provided.
    """
    email = serializers.EmailField(required=False, allow_blank=True)
    
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username', 'email', 'password', 're_password')
    
    def validate_email(self, value):
        """Email is optional - return empty string if not provided"""
        return value if value else ''
    
    def create(self, validated_data):
        """Create user with auto-generated email if not provided"""
        email = validated_data.get('email', '')
        
        # If no email provided, generate one
        if not email:
            email = f"{validated_data['username']}@fracture-app.local"
        
        # Remove re_password as it's not a model field
        validated_data.pop('re_password', None)
        validated_data['email'] = email
        
        user = User.objects.create_user(**validated_data)
        return user

