# Generated by Django 3.1.4 on 2021-02-04 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airlines', '0021_auto_20210202_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='transit',
        ),
        migrations.AlterField(
            model_name='flight',
            name='days',
            field=models.ManyToManyField(blank=True, null=True, to='airlines.Current'),
        ),
    ]
