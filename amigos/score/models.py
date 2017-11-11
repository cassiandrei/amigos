from django.db import models
from accounts.models import User, Match, MatchManager

# Create your models here.

class Friendship(models.Model):
    points = models.IntegerField(default=0)
    user_id = models.IntegerField(null=False)
    match = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matches"
        ordering = ['-points']

    objects = MatchManager()