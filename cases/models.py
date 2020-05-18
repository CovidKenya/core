from django.db import models

class Country(models.Model):
        name = models.CharField(max_length=255, unique=True)
        slug = models.SlugField(unique=True)
        time_created = models.DateTimeField(auto_now_add=True)
        last_updated = models.DateTimeField(auto_now=True)

        class Meta:
            ordering = ['name']

        def __str__(self):
            return f'{self.name}'

class Visual(models.Model):
        date = models.DateField()
        cases = models.IntegerField()
        deaths = models.IntegerField()
        recovered = models.IntegerField()
        country =  models.ForeignKey(Country, related_name='visuals', on_delete=models.CASCADE)
        time_created = models.DateTimeField(auto_now_add=True)
        last_updated = models.DateTimeField(auto_now=True)

        class Meta:
            ordering = ['-date']

        def __str__(self):
            return f'{self.date} {self.cases}'

# class County(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     slug = models.SlugField(unique=True)
#     time_created = models.DateTimeField(auto_now_add=True)
#     last_updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ['name']

#     def __str__(self):
#             return f'{self.name}'

# class Subcounty(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     slug = models.SlugField(unique=True)
#     time_created = models.DateTimeField(auto_now_add=True)
#     last_updated = models.DateTimeField(auto_now=True)
#     county =  models.ForeignKey(County, related_name='county', on_delete=models.CASCADE)

#     class Meta:
#         ordering = ['name']

#     def __str__(self):
#             return f'{self.name}'

# class KenyanCase(models.Model):
#     date = models.DateField()
#     cases = models.IntegerField()
#     death = models.IntegerField()
#     recovered = models.IntegerField()
#     county =  models.ForeignKey(County, related_name='subcounty', on_delete=models.CASCADE)
#     #
#     time_created = models.DateTimeField(auto_now_add=True)
#     last_updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ['-date', 'county']
#         unique_together = [['date', 'county']]

#     def __str__(self):
#         return f'{self.county} {self.date}'
