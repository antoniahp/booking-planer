# Generated by Django 4.1.2 on 2023-04-19 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommodel',
            name='total_rooms',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
