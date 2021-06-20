from django.contrib.auth.models import User
from django.db import models


class Aboutall(models.Model):
    post_title = models.CharField(max_length=100)
    post_description = models.CharField(max_length=250)
    post_fulltext = models.TextField()
    # post_author = models.ForeignKey(User, on_delete=models.CASCADE,)
    post_author = models.CharField(max_length=50)
    post_create_at = models.DateField()

    def __str__(self):
        return self.post_title # to show title instead 'Object 1'