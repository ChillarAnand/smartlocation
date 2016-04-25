from rest_framework import serializers

from . import models


class ProviderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Provider
        fields = ('name', 'email', 'language', 'phone_number', 'currency', 'pk')


class ServiceAreaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.ServiceArea
        fields = ('provider', 'name', 'price', 'polygon', 'pk')
