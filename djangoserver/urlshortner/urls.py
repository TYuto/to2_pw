from django.urls import path, include
from . import views
from .v2 import v2urls

urlpatterns = [
    path('api/urls/', views.urls.as_view()),
    path('api/domains/', views.domains.as_view()),
    path('api/user/', views.getuser),
    path('api/gen_200/', views.gen_200),
    path('<str:rand>/', views.redirectView),
    path('api/v2/', include(v2urls), name='v2api'),
    path('<str:rand>', views.redirectView)
]
