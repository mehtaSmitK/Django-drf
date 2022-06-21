import imp
from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from app.models import Employee
from app.serializers import EmployeeSerializer
class EmployeeViewSet(ViewSet):
    def list(self,request):
        qs = Employee.objects.all()
        serializer = EmployeeSerializer(qs,many=True)
        return Response(serializer.data)
    def retrieve(self,request,pk=None):
        id = pk
        if pk:
            qs = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(qs)
            return Response(serializer.data)
    def create(self,request):
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

    def update(self,request,pk):
        """
        payload 1- {
                        "eno":1,
                        "ename":"smit",
                        "esal":200000,
                        "eaddr":"Ahmedabad"
                    }
        """
        id = pk
        qs = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(qs,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=400)
    def destroy(self,request,pk):
        id = pk
        qs = Employee.objects.get(pk=id)
        qs.delete()
        return Response({"meg":"Data Deleted"})


from rest_framework.viewsets import ModelViewSet
class EmployeeModelViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer