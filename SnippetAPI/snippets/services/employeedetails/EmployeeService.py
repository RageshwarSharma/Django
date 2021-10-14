from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from snippets import serializers
from snippets.models import Employee
from snippets.models.EmployeeModel import Employee
from snippets.serializers import EmployeeSerializer
from snippets.serializers.employeeserializer import EmployeeSerializer

class EmployeeService(APIView):
    def get_employee(self,request,format=None):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return({'data':serializer.data,'code':status.HTTP_200_OK,'message':'get all details'})

    def post_employee(self,request,format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return({'data':serializer.data,'code':status.HTTP_201_CREATED,'message':'posted details'})
        return({'data':serializer.data,'code':status.HTTP_400_BAD_REQUEST,'message':'return not found'})

    def get_employee_by_pk(self,request,pk,format=None):
        try:
            employee = Employee.objects.get(id=pk)
            serializer = EmployeeSerializer(employee)
            return({'data':serializer.data,'code':status.HTTP_200_OK,'message':'get details by id'})
        except Employee.DoesNotExist:
            return({'data':None,'code':status.HTTP_404_NOT_FOUND, 'message':'return not found'})

    def put_employee(self, request,pk, format=None):
        employee = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ({'data':serializer.data,'code':status.HTTP_200_OK,'message':'created details successfully'})
        return({'data':serializer.data,'code':status.HTTP_404_NOT_FOUND,'message':'return not found'})

    def delete_employee(self,request,pk,format=None):
        try:
            employee = Employee.objects.get(id=pk)
            employee.delete()
            return({'data':None,'code':status.HTTP_204_NO_CONTENT,'message':'deleted successfully'})
        except Employee.DoesNotExist:
            return({'data':None,'code':status.HTTP_404_NOT_FOUND,'message':'page not found'})