from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class InCategory(models.Model):
    name = models.CharField(max_length=40, unique=True)
    color = models.CharField(max_length=6, unique=True, default='88ff88')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Income Category'

class OutCategory(models.Model):
    name = models.CharField(max_length=40, unique=True)
    color = models.CharField(max_length=6, unique=True, default='ff8888')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Expense Category'

class Income(models.Model):
    category = models.ForeignKey(InCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    date = models.DateTimeField()

    class_name = "Income" #bad thing

    def __str__(self):
        return '[{}] {} +{}₴ | {}'.format(self.user, self.category, self.amount, self.date.date())
    
    class Meta:
        ordering = ('-date',)

class Expense(models.Model):
    category = models.ForeignKey(OutCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    date = models.DateTimeField()

    class_name = "Expense" #bad thing
    
    def __str__(self):
        return '[{}] {} -{}₴ | {}'.format(self.user, self.category, self.amount, self.date.date())

    class Meta:
        ordering = ('-date',)
