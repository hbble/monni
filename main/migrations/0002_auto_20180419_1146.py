# Generated by Django 2.0.1 on 2018-04-19 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incategory',
            name='name',
            field=models.CharField(default='88ff88', max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='outcategory',
            name='name',
            field=models.CharField(default='ff8888', max_length=40, unique=True),
        ),
    ]