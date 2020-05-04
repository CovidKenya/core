from django.db import models

class Cases(models.Model):
   date = models.DateField(auto_now_add=False)
   country = models.CharField (max_length=50)
   Region = models.CharField(max_length=50)