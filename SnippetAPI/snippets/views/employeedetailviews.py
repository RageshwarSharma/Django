from rest_framework.views import APIView
from snippets.models import Employee
from snippets.serializers import EmployeeSerializer
from rest_framework.response import Response
from snippets.services.employeedetails import EmployeeSerializer
from snippets.services.employeedetails.EmployeeService import EmployeeService

employee_obj = EmployeeService()

class GetEmployeeListView(APIView):
    def get(self, request, format=None):
        result = employee_obj.get_employee(request,format=None)
        return Response(result,status=result['code'])

class PostEmployeeListView(APIView):
    def post(self,request,format=None):
        result = employee_obj.post_employee(request,format=None)
        return Response(result,status=result['code'])

class RetrieveEmployeeListView(APIView):
    def get(self,request,fromat=None):
        result = employee_obj.get_employee_by_pk(request,format=None)
        return Response(result,status=result['code'])

class PutEmployeeListView(APIView):
    def put(self,request,format=None):
        result = employee_obj.put_employee(request,format=None)
        return Response(result,status=result['code'])

class DeleteEmployeeListView(APIView):
    def delete(self,request,format=None):
        result = employee_obj.delete_employee(request,format=None)
        return Response(result, status=result['code'])

        