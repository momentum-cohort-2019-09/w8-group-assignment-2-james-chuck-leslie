from rest_framework import serializers
from snipp_dogg.models import User, CodeSnippet

class CodeSnippetSerializer(serializers.ModelSerializer):
   class Meta:
       model = CodeSnippet
       fields = ['description', 'body', 'language', 'date_created', 'date_updated']

class UserSerializer(serializers.ModelSerializer):
   class Meta:
       pinned_snippets = CodeSnippetSerializer(many=True, read_only=True)
       model = User
       fields = ['profile_description', ]

