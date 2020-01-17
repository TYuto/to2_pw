from django.contrib import admin

from .models import Url, Domain


@admin.register(Url)
@admin.register(Domain)
class UrlAdmin(admin.ModelAdmin):
    pass

class DomainAdmin(admin.ModelAdmin):
    pass