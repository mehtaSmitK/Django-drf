from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.
def emp_data_view(request):
    emp_data={
        'eno':100,
        'ename':"smit",
        'esal':100000,
        'eaddr':'Mumbai',
    }
    return HttpResponse(emp_data)
import json
def emp_data_jsonview(request):
    emp_data={
        'eno':100,
        'ename':"smit",
        'esal':100000,
        'eaddr':'Mumbai',
    }
    return HttpResponse(json.dumps(emp_data),content_type='application/json')

from django.http import JsonResponse
def emp_data_jsonview2(request):
    emp_data={
        'eno':100,
        'ename':"smit",
        'esal':100000,
        'eaddr':'Mumbai',
    }
    return JsonResponse(emp_data)
