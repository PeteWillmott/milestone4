from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from .models import Billing_Address, Customer, Delivery_Address


class Billing_AddressForm(forms.ModelForm):
    class Meta:
        model = Billing_Address
        fields = [
            'billing_name',
            'street1',
            'street2',
            'town',
            'county',
            'postcode',
            'country'
        ]


class Customer_Form(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'title'
        ]


class Recipient_Form(forms.ModelForm):
    recipient = forms.ModelChoiceField(queryset=Delivery_Address.objects.all().only('street1'), widget=forms.RadioSelect, empty_label=None)
    class Meta:
        model = Delivery_Address
        fields = [
            'recipient'
        ]

    def clean_default(self):
        recipient = self.cleaned_data.get('recipient')
        return recipient


class Delivery_AddressForm(forms.ModelForm):
    class Meta:
        model = Delivery_Address
        labels = {'delivery_name': 'Recipient\'s name'}
        fields = [
            'title',
            'delivery_name',
            'street1',
            'street2',
            'town',
            'county',
            'postcode',
            'country'
        ]