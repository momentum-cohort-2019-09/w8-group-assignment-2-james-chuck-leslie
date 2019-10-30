from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

def homepage(request):
    return render(request, 'snipp_dogg/homepage.html')

@login_required
def profile(request):
    return render(request, "snipp_dogg/profile.html")
