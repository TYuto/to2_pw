from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Url(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    tempuser_id = models.UUIDField(blank=True,null=True)
    original_url = models.URLField(max_length=1000)
    # http://domain.com/hoge
    shorten_url = models.CharField(max_length=50, unique=False)
    # domain.com/random_
    validity_period = models.IntegerField()
    expiration_date = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.shorten_url +':'+ self.original_url

class Domain(models.Model):
    host = models.CharField(max_length=20) # localhost:3000
    enable_hours = models.BooleanField()
    enable_week = models.BooleanField()
    enable_month = models.BooleanField()
    def __str__(self):
        hours = '3時間' if self.enable_hours else ''
        week = '5日間' if self.enable_week else ''
        month = '5ヶ月' if self.enable_month else ''
        return self.host + ','.join([hours, week, month])

    