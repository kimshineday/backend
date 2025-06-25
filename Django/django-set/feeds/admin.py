from django.contrib import admin

# Register your models here.
from .models import Feed

@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    pass