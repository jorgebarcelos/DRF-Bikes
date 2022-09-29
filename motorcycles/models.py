from django.db import models

# Create your models here.
class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Bikes(Base):
    model_name = models.CharField(max_length=100, unique=True)
    engine_power = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Bike"
        verbose_name_plural = "Bikes"
        ordering = ['id']

    def __str__(self):
        return self.model_name


class Rating(Base):
    bike = models.ForeignKey(Bikes, related_name="ratings", on_delete=models.CASCADE)
    person_name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField(blank=True, default="")
    score = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = "Score"
        verbose_name_plural = "Scores"
        unique_together = ["email", "bike"]
        ordering = ['id']

    def __str__(self):
        return f"{self.person_name} reted {self.bike} with the score {self.score}"
