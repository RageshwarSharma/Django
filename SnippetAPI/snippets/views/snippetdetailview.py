from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from snippets.services.snippetdetails import SnippetService

snippet_obj = SnippetService()

class GetSnippetListView(APIView):
    def get(self,request,format=None):
        result = snippet_obj.get_snippet(request,format=None)
        return Response(result,status = result['code'])

class PostSnippetListView(APIView):
    def post(self,request,format=None):
        result = snippet_obj.post_snippet(request,format=None)
        return Response(result,status=result['code'])
    
class GetSnippetDetailView(APIView):
    def get(self,request,pk,format=None):
        result = snippet_obj.get_snippet_by_pk(request,format=None)
        return Response(result,status=result['code'])

class PutSnippetDetailView(APIView):
    def put(self,request,pk,format=None):
        result = snippet_obj.put_snippet(request,format=None)
        return Response(result,status=result['code'])

class DeleteSnippetView(APIView):
    def delete(self,request,pk,format=None):
        result=snippet_obj.delete_snippet(request,format=None)
        return Response(result,status=result['code'])
