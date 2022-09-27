from rest_framework import serializers
from .models import Bikes, Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {"email": {"write_only": True}}

        model = Rating
        fields = "__all__"


class BikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bikes
        fields = "__all__"
