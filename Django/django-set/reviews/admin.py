from django.contrib import admin

# Register your models here.
from .models import Review

@admin. register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass