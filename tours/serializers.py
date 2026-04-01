from rest_framework import serializers
from .models import Tour, TourImage, GalleryImage


class TourImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourImage
        fields = '__all__'


class TourSerializer(serializers.ModelSerializer):
    images = TourImageSerializer(many=True, read_only=True)

    class Meta:
        model = Tour
        fields = '__all__'


class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = '__all__'