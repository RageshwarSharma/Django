from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework.views import APIView
from snippets.models import Student
from snippets.models.StudentModel import Student
from snippets.serializers import StudentSerializer
from snippets.serializers.studentserializer import StudentSerializer

class StudentService(APIView):
    def get_student(self,request,format=None):
        student = Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        return({'data':serializer.data,'code':status.HTTP_200_OK,'message':'student details'})

    def get_student_by_pk(self,reqest,pk,format=None):
        try:
            student = Student.objects.get(id=pk)
            serializer = StudentSerializer(student)
            return({'data':serializer.data,'code':status.HTTP_200_OK,'message':'get details by id'})
        except Student.DoesNotExist:
            return({'data':None,'code':status.HTTP_400_BAD_REQUEST,'message':'not found'})

    def post_student(self,request,format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return({'data':serializer.data,'code':status.HTTP_201_CREATED,'message':'posted details'})
        return({'data':serializer.data,'code':status.HTTP_400_BAD_REQUEST,'message':'return not found'})

    def put_student(self,request,pk,format=None):
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return({'data':serializer.data,'code':status.HTTP_200_OK,'message':'put student'})


    def delete_student(self,request,pk,format=None):
        try:
            student = Student.objects.get(id=pk)
            student.delete()
            return({'data':None,'code':status.HTTP_204_NO_CONTENT,'message':'student deleted'})
        except Student.DoesNotExist:
            return({'data':None,'code':status.HTTP_400_BAD_REQUEST,'message':' return not found'})

