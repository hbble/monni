from django.db import models
from django.contrib.auth.models import User

class InCategory(models.Model):
    name = models.CharField(max_length=40, unique=True)
    color = models.CharField(max_length=6, unique=True, default='88ff88')

    def __str__(self):
        return self.name

class OutCategory(models.Model):
    name = models.CharField(max_length=40, unique=True)
    color = models.CharField(max_length=6, unique=True, default='ff8888')

    def __str__(self):
        return self.name

class Incomes(models.Model):
    category = models.ForeignKey(InCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.amount

class Expenses(models.Model):
    category = models.ForeignKey(OutCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)


