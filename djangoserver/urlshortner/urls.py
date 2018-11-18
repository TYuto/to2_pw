from django.urls import path, include
from . import views

urlpatterns = [
    path('urls/', views.urls.as_view()),
    path('<str:domain>/<str:rand>/', views.redirectView)
]
