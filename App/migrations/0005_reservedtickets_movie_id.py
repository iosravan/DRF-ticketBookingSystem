# Generated by Django 4.0.4 on 2022-05-24 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_tickets_movie_id_alter_tickets_movie_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservedtickets',
            name='movie_id',
            field=models.CharField(default='M-0000', max_length=50),
        ),
    ]
