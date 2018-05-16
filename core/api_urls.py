from django.urls import path
from . import api_views


app_name = 'core_api'
urlpatterns = [
    path('customer/', api_views.customer_list, name='customer_list'),
    path('customer/<int:customer_id>)/logs', api_views.customer_and_log,
         name='customer_and_log'),
    path('customer/search', api_views.search_customer, name='search_customer'),
    path('customer/filter_logs', api_views.filter_logs, name='filter_logs'),
    path('customer/register', api_views.register_customer, name='register_customer'),
    path('customer/register_and_log', api_views.register_and_log, name='register_and_log'),
]