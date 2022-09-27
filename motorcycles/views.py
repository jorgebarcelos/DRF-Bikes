from rest_framework import generics
from .models import Bikes, Rating
from .serializers import BikesSerializer, RatingSerializer

# Create your views here.


class BikesApiView(generics.ListCreateAPIView):
    queryset = Bikes.objects.all()
    serializer_class = BikesSerializer


class BikeApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bikes.objects.all()
    serializer_class = BikesSerializer


class RatingsApiView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class RatingApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer