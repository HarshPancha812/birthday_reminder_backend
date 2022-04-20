from pyexpat import model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from api.models import birthday_data

class TodoAdmin(admin.ModelAdmin):
  list_display = ('name', 'id', 'user_id','date')

admin.site.register(birthday_data, TodoAdmin)