from django.urls import path
from . import api_views


app_name = 'core_api'
urlpatterns = [
    path('customer/', api_views.customer_list, name='customer_list'),

]