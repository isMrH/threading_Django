from django.shortcuts import render
from .models import SQLlist,datalist
from django.views.decorators.csrf import csrf_exempt
import datetime
from .sql_select import threads_main
import time
# Create your views here.
def dataquery(request,error=''):
    sql_list = SQLlist.objects.all()
    return render(request,'data_query/index2.html',context={ 'sql_list':sql_list,'error':error})


@csrf_exempt
def selectlist(request):

    # if 'select' in request.POST and request.POST['starttime'] and request.POST['endtime']:
    select=request.POST.getlist("select")
    starttime = request.POST['starttime']
    endtime = request.POST['endtime']
    starttime1 = datetime.datetime.strptime(starttime, "%Y-%m-%d %H:%M")
    endtime1 = datetime.datetime.strptime(endtime, "%Y-%m-%d %H:%M")
    data_list = threads_main(select=select, starttime1=starttime1, endtime1=endtime1)
    return render(request,'data_query/selectlist.html',context={ 'data_list':data_list })
