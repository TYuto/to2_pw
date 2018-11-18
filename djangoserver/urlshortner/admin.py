from django.contrib import admin

from .models import Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    pass