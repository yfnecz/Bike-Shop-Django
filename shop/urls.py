from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path('bikes/', views.list_bikes, name='list'),
    path('bikes/<int:pk>/', views.BikeView.as_view(), name='bike_detail'),
    path('order/<int:pk>/', views.OrderView.as_view(), name='order_detail')
]
