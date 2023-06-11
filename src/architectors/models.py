from django.db import models


# Create your models here.

class Company(models.Model):
    title = models.CharField(max_length=10)
    number_of_employees = models.PositiveIntegerField()


class Architector(models.Model):
    name = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    is_active = models.BooleanField()
    company = models.ManyToManyField(Company)
