from snipp_dogg.models import User, CodeSnippet
from snipp_dogg.serializers import UserSerializer, CodeSnippetSerializer
from rest_framework import generics

# View to handle GET and POST requests

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CodeSnippetListCreate(generics.ListCreateAPIView):
    queryset = CodeSnippet.objects.all()
    serializer_class = CodeSnippetSerializer

class DetailSnippet(generics.RetrieveUpdateDestroyAPIView):
    queryset = CodeSnippet.objects.all()
    serializer_class =  CodeSnippetSerializer