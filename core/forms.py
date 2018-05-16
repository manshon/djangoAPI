from django import forms
from core.models import Customer


def create_error_dict_from_form_errors(form_errors):
    ret = {}
    for field_name, errors in form_errors.items():
        ret[field_name] = []
        for error in errors:
            ret[field_name].append(error)
    return ret


class RegisterCustomerAPIForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = (
            'name',
            'email',
            'age',
        )


class RegisterCustomerAndLogAPIForm(forms.ModelForm):

    note = forms.CharField()
    amount = forms.IntegerField()

    class Meta:
        model = Customer
        fields = (
            'name',
            'email',
            'age',
        )