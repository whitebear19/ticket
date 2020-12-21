from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class EmployeeAdmin(UserAdmin):
    pass
# admin.site.register(CustomUser)
admin.site.register(CustomUser, EmployeeAdmin)
# Register your models here.
