from django.template import loader
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from .forms import diposit_form
from ..models import money_entry_data
import datetime

class entry_data(View):
    def get(self, request):
        form = diposit_form()
        return render(request, 'dipositForm.html', {'form': form})

def status_display(request):
    if request.method == 'POST':
        now =datetime.datetime.now()
        name=request.POST.get('name')
        account_no=request.POST.get('account_no')
        amount=request.POST.get('amount')
        hour=now.hour
        minute=now.minute
        time=hour*60+minute
        start_time=10*60
        end_time=17*60
 # 17 means 5PM then convert minutes

        if time >= start_time and time<=end_time:
                    diposit_data=money_entry_data(name=name,account_no=account_no,amount=amount)
                    diposit_data.save()
                    context={
                         'hour':hour,
                         'minute':minute,
                    }
                    template=loader.get_template('accepted.html')
                    return HttpResponse(template.render(context,request))
        else:
             context={
                    'hour':hour,
                    'minute':minute,
             }
             template=loader.get_template('timeEnd.html')
             return HttpResponse(template.render(context,request))


class transactions_statement(View):
    template=loader.get_template('statements.html')
    datalist=money_entry_data.objects.all().values()
    context={
        'datalist':datalist
    }
    def get(self,request):
        return HttpResponse(self.template.render(self.context,request))
