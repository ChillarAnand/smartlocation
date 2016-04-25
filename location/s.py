from .models import Provider
from django.contrib.auth.models import User
from rest_framework import serializers


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        exclude = ('user',)


class UserSerializer(serializers.ModelSerializer):
    provider = ProviderSerializer(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'language')

    def create(self, validated_data):
        profile_data = validated_data.pop('provider')
        user = User.objects.create(**validated_data)
        Provider.objects.create(user=user, **profile_data)
        return user
