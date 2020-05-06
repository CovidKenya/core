from django.db import models


class Cases(models.Model):
   date = models.DateField(auto_now_add=False)
   country = models.CharField (max_length=50)
   Region = models.CharField(max_length=50)

    
class Visuals(models.Model):
    country = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    timeline = models.TextField(max_length=None)

    def __str__(self):
        return f'{self.country} {self.province} {self.timeline}'

