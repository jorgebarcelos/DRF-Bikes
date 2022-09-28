from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (
    BikesApiView,
    RatingApiView,
    BikeApiView,
    RatingsApiView,
    BikesViewSet,
    RatingViewSet,
)

router = SimpleRouter()
router.register('bikes', BikesViewSet)
router.register('ratings', RatingViewSet)


urlpatterns = [
    path("bikes/", BikesApiView.as_view(), name="bikes"),
    path("bikes/<int:pk>", BikeApiView.as_view(), name="bike"),
    path("bikes/<int:bike_pk>/ratings", RatingsApiView.as_view(), name="bike_ratings"),
    path(
        "bikes/<int:bike_pk>/ratings/<int:rating_pk>/",
        RatingsApiView.as_view(),
        name="bike_rating",
    ),
    path("ratings/", RatingsApiView.as_view(), name="ratings"),
    path("ratings/<int:rating_pk>", RatingApiView.as_view(), name="rating"),
]
