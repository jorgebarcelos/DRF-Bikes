from django.urls import path
from .views import BikesApiView, RatingApiView, BikeApiView, RatingsApiView

urlpatterns = [
    path('bikes/', BikesApiView.as_view(), name='bikes'),
    path('bikes/<int:pk>', BikeApiView.as_view(), name='bike'),
    path('ratings/', RatingsApiView.as_view(), name='ratings'),
    path('ratings/<int:pk>', RatingApiView.as_view(), name='rating'),
]