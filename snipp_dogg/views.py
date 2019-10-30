from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from snipp_dogg.models import CodeSnippet
from snipp_dogg.forms import SnippDogdUserCreationForm, CreateSnippForm

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

def edit_snipp(request, pk):
    og_snipp = get_object_or_404(CodeSnippet, id=pk)
    if request.method == 'POST':
        form = CreateSnippForm(request.POST)
        if form.is_valid():
            snipp = form.save(commit=False)
            snipp.source = og_snipp
            snipp.user = request.user
            snipp.save()
            messages.success(request, f'Your Snipp has Been Edited!')
            return redirect('homepage')
    else:
        form = CreateSnippForm()
    return render(request, "snipp_dogg/create.html",{
        "form": form
    })

def homepage(request):
    return render(request, 'snipp_dogg/homepage.html')

@login_required
def profile(request):
    return render(request, "snipp_dogg/profile.html")
