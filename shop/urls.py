from django.urls import path
from . import views


urlpatterns = [
    path("", views.MainView.as_view()),
    path('bikes/', views.list_bikes, name='list'),
    path('bikes/<int:pk>/', views.BikeView.as_view(), name='bike_detail')
]
