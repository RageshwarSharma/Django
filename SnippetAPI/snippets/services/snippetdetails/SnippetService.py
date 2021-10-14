from django.core.checks import messages
from django.db.models import manager
from django.shortcuts import render
from rest_framework import parsers, status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from snippets import serializers
import snippets
from snippets.models import Snippet
from snippets.models.SnippetModel import Snippet
from snippets.serializers import SnippetSerializer
from snippets.serializers.snippetserializer import SnippetSerializer

class SnippetService(APIView):
    def get_snippet(self,request,format=None):
        snippet = Snippet.objects.all()
        serializer = SnippetSerializer(snippet,many=True)
        return({'data':serializer.data,'code':status.HTTP_200_OK,'message':'Snippet get successfully'})

    def post_snippet(self,request,format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return({'data':serializer.data,'code':status.HTTP_201_CREATED,'message':'Snippet Post success'})
        return({'data':serializer.data,'code':status.HTTP_400_BAD_REQUEST,'message':'Snippet page not found'})

    def get_snippet_by_pk(self,request,pk,format=None):
        try:
            snippet = Snippet.objects.get(pk=pk)
            serializer = SnippetSerializer(snippet)
            return({'data':serializer.data,'code':status.HTTP_200_OK,'message':'Snippet fetch id get data'})
        except Snippet.DoesNotExist:
            return({'data':None,'code':status.HTTP_400_BAD_REQUEST,'message':'Snippet Doesnot found'})

    def put_snippet(self,request,pk,format=None):
        snippet = self.get_snippet_by_pk(pk=pk)
        serializer = SnippetSerializer(snippet,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return({'data':serializer.data,'code':status.HTTP_201_CREATED,'message':'snippet updated'})

    def delete_snippet(self,request,pk,format=None):
        snippet = self.get_snippet_by_pk(pk=pk)
        snippet.delete()
        return({'data':None,'code':status.HTTP_204_NO_CONTENT,'message':'snippet deleted'})  

