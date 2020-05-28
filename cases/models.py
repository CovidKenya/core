from django.db import models


class VisualCountry(models.Model):
    """"
    Store Countries
    """
    name = models.CharField(max_length=255)
    #
    time_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class VisualData(models.Model):
    """
    Abstract Model
    """
    country = models.ForeignKey(VisualCountry, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class VisualCases(VisualData):
    date = models.DateField(null=True)
    cases = models.IntegerField(null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.country} {self.date} {self.cases}'


class VisualRecovered(VisualData):
    date = models.DateField(null=True)
    recovered = models.IntegerField(null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.country} {self.date} {self.recovered}'


class VisualDeaths(VisualData):
    date = models.DateField(null=True)
    deaths = models.IntegerField(null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.country} {self.date} {self.deaths}'


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
