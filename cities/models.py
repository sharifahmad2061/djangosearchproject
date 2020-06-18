from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'cities'
