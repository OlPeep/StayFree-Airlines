# Generated by Django 3.1.4 on 2021-01-10 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airlines', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='date',
            options={'ordering': ['date']},
        ),
        migrations.RenameField(
            model_name='flight',
            old_name='departure_time',
            new_name='time',
        ),
    ]