from django.contrib import admin

# Register your models here.
from .models import Bikes, Rating


@admin.register(Bikes)
class BikesAdmin(admin.ModelAdmin):
    list_display = [
        "model_name",
        "engine_power",
        "created_at",
        "updated_at",
        "is_active",
    ]


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = [
        "bike",
        "person_name",
        "email",
        "score",
        "created_at",
        "updated_at",
        "is_active",
    ]
