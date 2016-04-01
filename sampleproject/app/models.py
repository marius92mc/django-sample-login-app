from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

TRADER = 0
CENTRAL_BANK = 1

class MyUser(AbstractUser):
    type = models.IntegerField(default=0) 

class Currency(models.Model):
    name = models.CharField(max_length=16)
    country = models.CharField(max_length=64)

class CurrencyPair(models.Model):
    base_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='+')
    reporting_currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

