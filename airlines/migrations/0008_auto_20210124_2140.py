# Generated by Django 3.1.4 on 2021-01-24 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airlines', '0007_flight_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='days',
        ),
        migrations.AddField(
            model_name='flight',
            name='days',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='airlines.current'),
        ),
    ]
