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
    shorten_url = models.CharField(max_length=50, unique=True)
    # domain.com/random_
    validity_period = models.IntegerField()
    expiration_date = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.original_url

    