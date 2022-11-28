from rest_framework import serializers

from apps.cars.models import CarModel


class CarSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    model = serializers.CharField()
    year = serializers.IntegerField()
    seats = serializers.IntegerField()
    type_of_car = serializers.CharField()
    volume = serializers.FloatField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        car = CarModel.objects.create(**validated_data)
        return car


class CarSerializers2(serializers.Serializer):
    model = serializers.CharField()
    year = serializers.IntegerField()
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        car = CarModel.objects.create(**validated_data)
        return car
