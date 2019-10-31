from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
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
            snipp.source = og_snipp
            snipp.user = request.user
            snipp.date_updated = timezone.now()
            snipp.save()
            messages.success(request, f'Your Snipp has Been Edited!')
            return redirect('profile')
    else:
        form = CreateSnippForm()
        form.fields['language'].initial = og_snipp.language
        form.fields['body'].initial = og_snipp.body
        form.fields['description'].initial = og_snipp.description
    return render(request, "snipp_dogg/edit.html",{
        "form": form
    })

def homepage(request):
    snipps = CodeSnippet.objects.all()
    return render(request, 'snipp_dogg/homepage.html', {
        "snipps": snipps,
    })

@login_required
def profile(request):
    user_snipps = CodeSnippet.objects.filter(user=request.user)
    return render(request, "snipp_dogg/profile.html", {
        'snippets': user_snipps
    })
