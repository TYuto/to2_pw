from django.urls import path, include
from . import views

urlpatterns = [
    path('api/urls/', views.urls.as_view()),
    path('api/domains/', views.domains.as_view()),
    path('api/user/', views.getuser),
    path('api/gen_200/', views.gen_200),
    path('<str:rand>/', views.redirectView),
    path('<str:rand>', views.redirectView),
]
