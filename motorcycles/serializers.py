from rest_framework import serializers
from .models import Bikes, Rating
from django.db.models import Avg


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {"email": {"write_only": True}}

        model = Rating
        fields = "__all__"

    def validate_score(self, value):
        if value in range(1, 6):
            return value
        raise serializers.ValidationError("Score between 1 to 5")


class BikesSerializer(serializers.ModelSerializer):

    ratings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    average_ratings = serializers.SerializerMethodField()

    class Meta:
        model = Bikes
        fields = "__all__"

    def get_average_ratings(self, obj):
        average = obj.ratings.aggregate(Avg('score')).get('score__avg')

        if average is None:
            return 0
        return round(average * 2) / 2
