from django.db import models


class money_entry_data(models.Model):
    name=models.CharField(max_length=100)
    account_no=models.CharField(max_length=55)
    amount=models.CharField(max_length=100000)