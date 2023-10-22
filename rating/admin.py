from django.contrib import admin
from .models import MincePie, Ratings, Questions, MincePieRating

# Register your models here.

admin.site.register(MincePie)
admin.site.register(MincePieRating)
admin.site.register(Ratings)
admin.site.register(Questions)
