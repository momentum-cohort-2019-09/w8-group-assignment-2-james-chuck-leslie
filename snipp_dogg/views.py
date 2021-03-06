import re as re
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from snipp_dogg.serializers import CodeSnippetSerializer, UserSerializer
from snipp_dogg.models import CodeSnippet, User
from snipp_dogg.forms import SnippDogdUserCreationForm, CreateSnippForm, SearchForm

def register_user(request):
    if request.method == 'POST':
        form = SnippDogdUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Account has Been Created! You May Now Login!')
            return redirect('login')
    else:
        form = SnippDogdUserCreationForm()
    return render(request, "snipp_dogg/register.html",{
        "form": form
    })


@login_required
def snipp_detail(request, pk):
    snipp = CodeSnippet.objects.get(id=pk)
    return render(request, 'snipp_dogg/snipp_detail.html', {
        "snipp": snipp,
    })

@login_required
def create_snipp(request):
    if request.method == 'POST':
        form = CreateSnippForm(request.POST)
        if form.is_valid():
            snipp = form.save(commit=False)
            snipp.user = request.user
            snipp.save()
            messages.success(request, f'Your Snipp has Been Created!')
            return redirect('profile')
    else:
        form = CreateSnippForm()
    return render(request, "snipp_dogg/create.html",{
        "form": form
    })

@login_required
def edit_snipp(request, pk):
    og_snipp = get_object_or_404(CodeSnippet, id=pk)
    if request.method == 'POST':
        form = CreateSnippForm(request.POST)
        if form.is_valid():
            snipp = form.save(commit=False)
            snipp.date_updated = timezone.now()
            snipp.user = request.user
            snipp.save()
            og_snipp.delete()
            messages.success(request, f'Your Snipp has Been Edited!')
            return redirect('profile')
    else:
        form = CreateSnippForm()
        form.fields['title'].initial = og_snipp.title
        form.fields['language'].initial = og_snipp.language
        form.fields['body'].initial = og_snipp.body
        form.fields['description'].initial = og_snipp.description
    return render(request, "snipp_dogg/edit.html",{
        "form": form
    })

def homepage(request):
    return render(request, 'snipp_dogg/homepage.html')

@login_required
def profile(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            if data.get('search_choice') == 'language':
                user_snipps = CodeSnippet.objects.filter(user=request.user, language=data.get('search_text'))
                form = SearchForm()
                return render(request, "snipp_dogg/profile.html", {
                    'snippets': user_snipps,
                    'form': form,
                    'searched': True
                })
            elif data.get('search_choice') == 'title':
                selected_snipps = []
                all_user_snipps = CodeSnippet.objects.filter(user=request.user)
                title_regex = r"" + re.escape(data.get('search_text'))
                for snipp in all_user_snipps:
                    if re.search(title_regex, snipp.title, re.IGNORECASE):
                        selected_snipps.append(snipp)
                form = SearchForm()
                return render(request, "snipp_dogg/profile.html", {
                    'snippets': selected_snipps,
                    'form': form,
                    'searched': True
                })
            elif data.get('search_choice') == 'description':
                selected_snipps = []
                all_user_snipps = CodeSnippet.objects.filter(user=request.user)
                descrip_regex = r"" + re.escape(data.get('search_text'))
                for snipp in all_user_snipps:
                    if re.search(descrip_regex, snipp.description, re.IGNORECASE):
                        selected_snipps.append(snipp)
                form = SearchForm()
                return render(request, "snipp_dogg/profile.html", {
                    'snippets': selected_snipps,
                    'form': form,
                    'searched': True
                })
    else:
        user_snipps = CodeSnippet.objects.filter(user=request.user)
        form = SearchForm()
        return render(request, "snipp_dogg/profile.html", {
            'snippets': user_snipps,
            'form': form
        })

def delete_snipp(request, pk):
    snipp = get_object_or_404(CodeSnippet, id=pk)
    if request.method == "POST":
        snipp.delete()
        return redirect('profile')
    else:
        return render(request, 'snipp_dogg/delete.html', {
            "snipp": snipp,
        })

# API Views

class SnippList(APIView):
    """
    List all snippets, or create a new snippet
    """

    def get(self, request, format=None):
        snipps = CodeSnippet.objects.all()
        serializer = CodeSnippetSerializer(snipps, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CodeSnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SnippDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return CodeSnippet.objects.get(pk=pk)
        except CodeSnippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CodeSnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CodeSnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SnippByUser(APIView):
    """
    retrive all snipps by user
    """
    def get(self, request, username, format=None):
        user = User.objects.get(username=username)
        snipps = CodeSnippet.objects.filter(user=user)
        serializer = CodeSnippetSerializer(snipps, many=True)
        return Response(serializer.data)

class SnippByUserAndLanguage(APIView):
    """
    retrive snipps for user by language
    """
    def get(self, request, username, language, format=None):
        user = User.objects.get(username=username)
        snipps = CodeSnippet.objects.filter(user=user, language=language)
        serializer = CodeSnippetSerializer(snipps, many=True)
        return Response(serializer.data)