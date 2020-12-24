from slugify import slugify
from rest_framework import serializers

from apps.locations.models import City, Country


class CountrySerializer(serializers.ModelSerializer):
    """ Serializer class for Country model """

    class Meta:
        model = Country
        fields = '__all__'
        read_only_fields = ('slug',)

    def validate_name(self, value):
        if Country.objects.filter(slug=slugify(value)).count() != 0 and self.instance.name != value:
            raise serializers.ValidationError('Name must be unique')
        return value

    def update(self, instance, validated_data):
        """ Method which updates city object """

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance


class CitySerializer(serializers.ModelSerializer):
    """ Serializer class for City model """
    country = serializers.SlugRelatedField(many=False, slug_field='slug', queryset=Country.objects.all())

    class Meta:
        model = City
        fields = '__all__'
        read_only_fields = ('slug',)

    def validate_name(self, value):
        if City.objects.filter(slug=slugify(value)).count() != 0 and self.instance.name != value:
            raise serializers.ValidationError('Name must be unique')
        return value

    def update(self, instance, validated_data):
        """ Method which updates city object """

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
