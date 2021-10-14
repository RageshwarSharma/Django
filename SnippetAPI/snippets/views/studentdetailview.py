from rest_framework.views import APIView
from rest_framework.response import Response
from snippets.models import Student
from snippets.serializers import StudentSerializer
from snippets.services.studentdetails import StudentService

student_obj = StudentService()

class GetStudentListView(APIView):
    def get(self,request,format=None):
        result = student_obj.get_student(request,format=None)
        return Response(result,status=result['code'])

class PostStudentListView(APIView):
    def post(self,request,format=None):
        result=student_obj.post_student(request,format=None)
        return Response(result, status=result['code'] )

class GetStudentDetailView(APIView):
    def get(self,request,format=None):
        result = student_obj.get_student_by_pk(request,format=None)
        return Response(result, status=result['code'])

class PutStudentlistView(APIView):
    def put(self,request,format=None):
        result=student_obj.put_student(request,format=None)
        return Response(result, status=result['code'])
        
class DeleteStudentListView(APIView):
    def delete(self,request,format=None):
        result = student_obj.delete_student(request,format=None)
        return Response(result, status=result['code'])