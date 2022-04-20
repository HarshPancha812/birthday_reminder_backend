from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import newuser
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models
# Register your models here.
class UserAdminConfig(UserAdmin):
    model = newuser
    search_fields = ('email', 'last_name', 'first_name',)
    list_filter = ('email', 'last_name', 'first_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'id','password','last_name', 'first_name',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'last_name', 'first_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
   
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','first_name', 'last_name','password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(newuser, UserAdminConfig)
