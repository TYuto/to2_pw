# Generated by Django 2.1.3 on 2018-11-18 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='tempuser_id',
            field=models.UUIDField(blank=True, null=True),
        ),
    ]