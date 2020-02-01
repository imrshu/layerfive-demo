from rest_framework import serializers
from .models import UserDescription


class UserDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDescription
        fields = '__all__'
