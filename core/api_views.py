from datetime import datetime
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from core.models import (
    Customer,
    CustomerLog,
)
from . import forms
from .forms import create_error_dict_from_form_errors


API_TOKEN = "dkwRNwBXq8HauWWUBesZBiuctRDBBJRneHNLzaBj4CAhZQrE"


def customer_list(request):
    """
    顧客情報を返すAPI
    :param request:
    :return:
    """
    if not request.GET.get("token") or request.GET["token"] != API_TOKEN:
        return JsonResponse({}, status=403)
    return JsonResponse([customer.to_dict() for customer in Customer.objects.all()], safe=False)


def customer_and_log(request, customer_id):
    """
    顧客の詳細情報と、その顧客の来店記録を全て返すAPI
    :param request:
    :param customer_id:
    :return:
    """
    customer = Customer.objects.get(id=customer_id).to_dict()
    customer['logs'] = CustomerLog.get_logs(customer_id)
    return JsonResponse(customer, safe=False)


def search_customer(request):
    """
    指定されたkeywordをname or emailに含む顧客を全て返す。keywordが指定されなければ、空のリスト([])を返す
    :param request:
    :return:
    """
    keyword = request.GET.get('keyword')
    customers = [customer.to_dict() for customer in Customer.search(keyword=keyword)]
    return JsonResponse(customers, safe=False)


def filter_logs(request):
    """
    開始日付から終了日付（それぞれを含む）で指定された期間に来店した来店記録のみを取得して、来店日時が古い順に返す
    :param request:
    :return:
    """
    params = request.GET.copy()
    from_ = params['from']
    to_ = params['to']
    customer_logs = [log.to_dict() for log in CustomerLog.filter_period(from_, to_)]
    return JsonResponse(customer_logs, safe=False)


@csrf_exempt
def register_customer(request):
    """
    Customerに新規登録するAPI
    :param request:
    :return:
    """
    form = forms.RegisterCustomerAPIForm(json.loads(request.body))
    if not form.is_valid():
        return JsonResponse(create_error_dict_from_form_errors(form.errors), status=400)
    form.save()
    return JsonResponse({})


def register_and_log(request):
    """
    顧客登録+初回訪問記録登録API
    :param request:
    :return:
    """
    form = forms.RegisterCustomerAndLogAPIForm(json.loads(request.body))
    if not form.is_valid():
        return JsonResponse(create_error_dict_from_form_errors(form.errors), status=400)
    customer = form.save()
    CustomerLog.objects.create(
        customer=customer,
        ammount=form.cleaned_data['amount'],
        note=form.cleaned_data['note'],
    )
    return JsonResponse({})