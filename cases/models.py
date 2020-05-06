from django.db import models


class Cases(models.Model):
    date = models.DateField(auto_now_add=False)
    country = models.CharField(max_length=50)
    Region = models.CharField(max_length=50)


class Visual(models.Model):
    """
    specified the country as the pk to allow for easy update/create
    https://docs.djangoproject.com/en/3.0/ref/models/instances/#the-pk-property
    """
    country = models.CharField(primary_key=True, max_length=255)
    case = models.TextField()
    death = models.TextField()
    recovery = models.TextField()
    #
    time_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['country']

    def __str__(self):
        return f'{self.country} {self.case}'
