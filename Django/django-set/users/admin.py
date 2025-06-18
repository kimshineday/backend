from django.contrib import admin

# Register your models here.
from .models import User

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['name', 'description', 'age', 'gender']
#     list_filter = ['age', 'gender']
#     search_fields = ['name']

from django.contrib.auth.admin import UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin): #user admin 기능을 가져옴
    list_display = ("username", "email", "is_business", "grade")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )