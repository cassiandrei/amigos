from django.db import models
from accounts.models import User, Match, MatchManager


# Create your models here.

class Friendship(models.Model):
    user_id = models.IntegerField(null=False)
    friend_id = models.IntegerField(null=False)

    class Meta:
        verbose_name = "Friendship"
        verbose_name_plural = "Friendships"