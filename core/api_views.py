from datetime import datetime
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from core.models import (
    Customer,
    CustomerLog,
)
from . import forms


API_TOKEN = "dkwRNwBXq8HauWWUBesZBiuctRDBBJRneHNLzaBj4CAhZQrE"


def customer_list(request):
    if not request.GET.get("token") or request.GET["token"] != API_TOKEN:
        return JsonResponse({}, status=403)
    return JsonResponse([customer.to_dict() for customer in Customer.objects.all()], safe=False)