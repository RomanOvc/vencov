from django.db import models

# Create your models here.

# человек
from rest_framework import serializers


class Citizen(models.Model):
    fullname = models.TextField(max_length=100)
    city = models.TextField(max_length=100)
    profession = models.TextField(max_length=100)
    age = models.IntegerField()


# доход
class Income(models.Model):
    citizen_id = models.ForeignKey(Citizen, on_delete=models.CASCADE, related_name='incomes')
    date = models.DateField()
    income = models.IntegerField()


class Persona(models.Model):
    fullname = models.TextField(max_length=100)
    city = models.TextField(max_length=100)
    age = models.IntegerField()
    club = models.TextField(max_length=100)
    vid_s = models.TextField(max_length=100)


class Zarplata(models.Model):
    citizen_id = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='zarplats')
    data = models.DateField()
    income = models.IntegerField()
