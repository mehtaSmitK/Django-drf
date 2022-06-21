from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from django.views.generic import View
import json
from django.core.serializers import serialize
# Create your views here.

class EmployeeCRUD(View):
    def get(self,request,id,*args,**kwargs):
        
        emp=Employee.objects.get(id=id)
        """
        #option 1
        data={
        'eno':emp.eno,
        'ename':emp.ename,
        'esal':emp.esal,
        'eaddr':emp.eaddr,
        }
        """
        #Option 2
        data = serialize("json",[emp])
        
        return HttpResponse(data,content_type='application/json')

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import EmployeeForm

@method_decorator(csrf_exempt,name="dispatch")
class EmployeeList(View):
    def get(self,request,*args,**kwargs):
        emp=Employee.objects.all()
        data = json.loads(serialize("json",emp))
        final_list = []
        for obj in data:
            emp_data = obj["fields"]
            final_list.append(emp_data)
        
        return HttpResponse(json.dumps(final_list),content_type='application/json')

    def post(self,request,*args,**kwargs):
        data=json.loads(request.body)
        form = EmployeeForm(data)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse(json.dumps({'msg':"sucess"}),content_type='application/json')
        return HttpResponse(json.dumps({'msg':"error"}),content_type='application/json')

    def put(self,request,*args,**kwargs):
        data=json.loads(request.body)
        emp  = Employee.objects.get(eno = data["eno"])
        form = EmployeeForm(data,instance=emp)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse(json.dumps({'msg':"sucess"}),content_type='application/json')
        return HttpResponse(json.dumps({'msg':"error"}),content_type='application/json')

    def delete(self,request,*args,**kwargs):
        data=json.loads(request.body)
        emp  = Employee.objects.get(eno = data["eno"])
        if emp!=None:
            emp.delete()
            return HttpResponse(json.dumps({'msg':"sucess"}),content_type='application/json')
        return HttpResponse(json.dumps({'msg':"error"}),content_type='application/json')



    
            