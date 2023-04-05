from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from .forms import data_entry_form
from django.views import View
from .models import money_entry_data
import datetime

def diposit_data(request):
    form = data_entry_form()
    return render(request, 'pages/diposit.html', {'form': form})


class status_displays(View):
    def get(self,request):
        if request.method == 'POST':
            name=request.POST.get('name')
        print('name is ',name)
        template=loader.get_template('pages/status.html')
        return HttpResponse(template.render())  
    
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
                    template=loader.get_template('pages/status.html')
                    return HttpResponse(template.render(context,request))
        else:
             context={
                    'hour':hour,
                    'minute':minute,
             }
             template=loader.get_template('pages/timeEnd.html')
             return HttpResponse(template.render(context,request))




class transactions_statement(View):
    template=loader.get_template('pages/transactions_details.html')
    datalist=money_entry_data.objects.all().values()
    context={
        'datalist':datalist
    }
    def get(self,request):
        return HttpResponse(self.template.render(self.context,request))
