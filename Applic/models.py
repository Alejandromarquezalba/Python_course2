from django.db import models

# Create your models here.


class Market(models.Model):
    money = models.CharField(max_length=100)
    client = models.IntegerField()
    def __str__(self):
        return f'{self.money}'

class Client(models.Model):
    money = models.CharField(max_length=100)
    product = models.IntegerField()
    def __str__(self):
        return f'{self.money}'

class Worker(models.Model):
    pay = models.CharField(max_length=100)
    hours = models.IntegerField()
    def __str__(self):
        return f'{self.pay}'