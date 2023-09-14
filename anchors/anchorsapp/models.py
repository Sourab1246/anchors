from django.db import models

# Create your models here.
class Video(models.Model):
    url=models.URLField(unique=True)

    def __str__(self):
        return self.url 
