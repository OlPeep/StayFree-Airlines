# Generated by Django 3.1.4 on 2021-01-24 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airlines', '0010_auto_20210124_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='days',
            field=models.ManyToManyField(to='airlines.Current'),
        ),
    ]
