from django.urls import path, include
from . import views

urlpatterns = [
    path('urls/', views.urls.as_view()),
    path('<str:domain>/<str:rand>/', views.redirectView),
    path('<str:domain>/<str:rand>', views.redirectView),
    path('user/', views.getuser),
    path('gen_200/', views.gen_200)
]
