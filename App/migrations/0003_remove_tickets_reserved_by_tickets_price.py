# Generated by Django 4.0.4 on 2022-05-24 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_reservedtickets_alter_tickets_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickets',
            name='Reserved_by',
        ),
        migrations.AddField(
            model_name='tickets',
            name='price',
            field=models.IntegerField(default=200),
        ),
    ]
