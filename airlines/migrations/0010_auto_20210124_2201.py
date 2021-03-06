# Generated by Django 3.1.4 on 2021-01-24 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airlines', '0009_auto_20210124_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='capacity',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='passengers',
        ),
        migrations.AddField(
            model_name='single',
            name='capacity',
            field=models.IntegerField(default=130),
        ),
        migrations.AddField(
            model_name='single',
            name='passengers',
            field=models.ManyToManyField(blank=True, to='airlines.Passenger'),
        ),
    ]
