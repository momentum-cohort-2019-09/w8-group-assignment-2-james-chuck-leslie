"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from snipp_dogg import api
from django.contrib.auth import views as auth_views
from snipp_dogg import views as snipp_views

urlpatterns = [
    path('', include('frontend.urls')),
    path('admin/', admin.site.urls),
    path('api/snipp_dogg/', api.CodeSnippetListCreate.as_view()),
    path('api/snipp_dogg/user', api.UserListCreate.as_view()),
    path('', snipp_views.homepage, name='homepage'),
    path('snipp_dogg/create', snipp_views.create_snipp, name='create'),
    path('snipp_dogg/edit', snipp_views.edit_snipp, name='edit'),
    path('snipp_dogg/profile', snipp_views.profile, name='profile'),
    path('snipp_dogg/register', snipp_views.register_user, name='register_user'),
    path('snipp_dogg/login', auth_views.LoginView.as_view(template_name='snipp_dogg/login.html'), name='login'),
    path('snipp_dogg/logout', auth_views.LogoutView.as_view(template_name='snipp_dogg/logout.html'), name='logout')
]
