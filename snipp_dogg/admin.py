from django.contrib import admin
from snipp_dogg.models import User, Language, CodeSnippet
from django.contrib.auth.admin import UserAdmin


admin.site.register(User, UserAdmin)
admin.site.register(Language)
admin.site.register(CodeSnippet)