from django.db import models


class Visual(models.Model):
    country = models.CharField(max_length=255)
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


class KenyanCase(models.Model):
    county = models.CharField(max_length=255)
    date = models.DateField()
    cases = models.IntegerField()
    death = models.IntegerField()
    recovery = models.IntegerField()
    #
    time_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', 'county']
        unique_together = [['date', 'county']]

    def __str__(self):
        return f'{self.county} {self.date}'
