from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/image')  # upload_to - where we will save image
    url = models.URLField(blank=True)  # blank=True - field  can be empty

    def __str__(self):
        return self.title # to show title instead 'Object 1'