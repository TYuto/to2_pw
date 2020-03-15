from django.urls import path, include
from .domains import domains

urlpatterns = [
    path('domains/', domains.as_view())
]
