from django.db import models


class MincePie(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    cost = models.FloatField()
    alcohol = models.BooleanField(default=False)
    amount_in_box = models.IntegerField()
    rating = models.IntegerField()
    price_per_pie = models.FloatField()
    times_rated = models.IntegerField()

    def __str__(self):
        return self.name


class Ratings(models.Model):
    pastry = models.IntegerField()

    def __str__(self):
        return self.pastry


class MincePieRating(models.Model):
    mince_pie = models.ForeignKey(MincePie, on_delete=models.CASCADE, related_name='ratings')
    rating_value = models.IntegerField()  # You can change this according to your rating system
    rated_by = models.CharField(max_length=100)  # You can replace this with your user model if you have one
    rated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('mince_pie', 'rated_by')  # Ensures each user can rate a MincePie only once


class Questions(models.Model):
    question = models.CharField(max_length=1000)
    comment = models.CharField(max_length=1000)
    value = models.IntegerField()

    def __str__(self):
        return self.question
