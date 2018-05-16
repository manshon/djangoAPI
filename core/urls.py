from django.urls import path
from . import views


app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('customer/<int:customer_id>/', views.customer_detail, name='customer_detail'),
]
