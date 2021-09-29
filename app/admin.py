from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class UserAdminConfig(UserAdmin):
    ordering = ('-start_date', )
    list_display = ('email', 'name', 'phone', 'is_active', 'is_staff')


admin.site.register(CustomUser, UserAdminConfig)
