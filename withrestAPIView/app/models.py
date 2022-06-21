from django.db import models

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal = models.FloatField(max_length=64)
    eaddr = models.CharField(max_length=64)