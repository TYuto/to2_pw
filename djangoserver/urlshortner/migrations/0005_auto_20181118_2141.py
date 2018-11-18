# Generated by Django 2.1.3 on 2018-11-18 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortner', '0004_url_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
