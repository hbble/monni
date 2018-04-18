from django.db import models
from django.contrib.auth.models import User

class InCategory(models.Model):
    name = models.CharField(max_length=40, unique=True)
    color = models.CharField(max_length=6, unique=True)

class OutCategory(models.Model):
    name = models.CharField(max_length=40, unique=True)
    color = models.CharField(max_length=6, unique=True)

class Earnings(models.Model):
    category = models.ForeignKey(InCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

class Outgoings(models.Model):
    category = models.ForeignKey(OutCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)


