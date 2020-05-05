from django.db import models

# Create your models here.


class Visuals(models.Model):
    country = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    timeline = models.TextField(max_length=None)

    def __str__(self):
        return self.country
        return self.province
        return self.timeline
