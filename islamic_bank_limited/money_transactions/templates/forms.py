from django import forms

class diposit_form(forms.Form):
    name = forms.CharField(max_length=100)
    account_no = forms.CharField(max_length=100)
    amount = forms.CharField(max_length=100000)