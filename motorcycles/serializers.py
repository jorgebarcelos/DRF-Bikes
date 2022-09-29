from rest_framework import serializers
from .models import Bikes, Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {"email": {"write_only": True}}

        model = Rating
        fields = "__all__"


class BikesSerializer(serializers.ModelSerializer):

    ratings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Bikes
        fields = "__all__"
