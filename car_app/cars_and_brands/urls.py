from django.urls import path
from . import views



urlpatterns = [
    path('', views.index),
    path('new/', views.add_brand),
    path('<int:id>/', views.view_brand),
    path('<int:id>/edit', views.edit_brand),
]