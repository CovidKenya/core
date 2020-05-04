from django.db import models

class Cases(models.Model)
   date = models.DateTimeField(auto_now_add=True)
   country = models.CharField (max_length=50)
   Region = models.CharField(max_length=50)