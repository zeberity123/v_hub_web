from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'is_creator']
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_creator=validated_data.get('is_creator', False)
        )
        return user

class SigninSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
