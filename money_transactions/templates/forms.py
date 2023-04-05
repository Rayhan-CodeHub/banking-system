# forms.py
from django import forms

class data_entry_form(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    account_no = forms.CharField(label='Your acc no', max_length=100)
    amount = forms.CharField(label='Your diposit amont', max_length=1000000)
