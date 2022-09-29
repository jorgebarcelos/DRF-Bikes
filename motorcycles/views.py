from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

from rest_framework.generics import get_object_or_404
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

    def get_queryset(self):
        if self.kwargs.get('bike_pk'):
            return self.queryset.filter(bike_id=self.kwargs.get('bike_pk'))
        return self.queryset.all()


class RatingApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_object(self):
        if self.kwargs.get('bike_pk'):
            return get_object_or_404(self.get_queryset(),
                                                        bike_id=self.kwargs.get('bike_pk'),
                                                        pk=self.kwargs.get('rating_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('rating_pk'))


class BikesViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Bikes.objects.all()
    serializer_class = BikesSerializer

    @action(detail=True, methods=['get'])
    def bike_ratings(self, request, pk=None):
        self.pagination_class.page_size = 1
        ratings = Rating.objects.filter(bike_id=pk)
        page = self.paginate_queryset(ratings)

        if page is not None:
            serializer = RatingSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)


class RatingViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer