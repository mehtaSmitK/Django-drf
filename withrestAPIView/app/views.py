from turtle import color
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from app.serializers import NameSerailizer
from app.models import Employee
from app.serializers import EmployeeSerializer
# Create your views here.

class TestAPI(APIView):
    def get(self,request,*args,**kwargs):
        colors = ["red","yellow","green","blue"]
        return Response({"msg":"Sample Rest API View","color":colors})

    def post(self,request,*args,**kwargs):
        """
        payload 1- {"name":"smit"}
        payload 2- {"fname":"smit"}
        """
        serializer = NameSerailizer(data=request.data)
        if serializer.is_valid():
            name= serializer.data.get("name")
            return Response({"msg":"hello, {}".format(name)})
        else:
            return Response(serializer.errors,status=400)
    def put(self,request,*args,**kwargs):
        # Write Custom Logic
        return Response({"msg":"Response from put APIView"})
    def delete(self,request,*args,**kwargs):
        # Write Custom Logic
        return Response({"msg":"Response from Delete APIView"})


class EmployeeAPIView(APIView):
    def get(self,request):
        qs = Employee.objects.all()
        serializer = EmployeeSerializer(qs,many=True)
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        """
        payload 1- {
                        "eno":1,
                        "ename":"smit",
                        "esal":200000,
                        "eaddr":"Ahmedabad"
                    }
        """
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors,status=400)

#####################LIST#####################
from rest_framework.generics import ListAPIView
class EmployeeListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeListAPIViewFilter(ListAPIView):
    #path - employee-list-apiview-filter/?ename=mehta
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get_queryset(self):
        name = self.request.GET.get("ename")
        if name:
            return super().get_queryset().filter(ename=name)
        return super().get_queryset()

#####################Create#####################
from rest_framework.generics import CreateAPIView
class EmployeeCreateAPIView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#####################Update#####################
#If you used Django Admin Panel to test data the use RetrieveUpdateAPIView insted of the UpdateAPIView
from rest_framework.generics import RetrieveUpdateAPIView
class EmployeeUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#####################Delete#####################
from rest_framework.generics import RetrieveDestroyAPIView
class EmployeeDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#####################CRUD#####################
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListCreateAPIView,GenericAPIView
class CRUDAPIView2(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
class CRUDAPIView1(GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = "id"


##################### MIXIN #####################
"""
It used for change the request data or chck the request data.
"""
from rest_framework.mixins import UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin
from rest_framework.generics import GenericAPIView 
class EmployeeCRUDMixin(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)
        
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)



