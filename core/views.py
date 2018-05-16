from django.shortcuts import render
from django.template.response import TemplateResponse

from .models import (
    Customer,
    CustomerLog,
)


def index(request):
    return render(request, "core/index.html", {
        "customer_list": Customer.objects.all(),
    })


def customer_detail(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    customer_logs = CustomerLog.objects.filter(customer=customer)

    return render(request, "core/customer_detail", {
        "customer": customer,
        "customer_logs": customer_logs,
    })
