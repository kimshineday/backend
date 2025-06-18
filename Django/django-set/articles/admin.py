from django.contrib import admin

# Register your models here.
from .models import Article
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin): # tuple의 형태
    list_display = ('title', 'writer', 'date', 'likes', 'content', 'updated_at', 'created_at')
    list_filter = ('date', 'writer')
    search_fields = ('title', 'content')
    ordering = ('-date',) # 목록페이지의 기본 정렬 순서 : 역순
    readonly_fields = ('writer',) # 읽기 전용 필드 지정, 수정이 안됨
    fieldsets = ( # 상세 페이지에서 필드 그룹 나눌 때
        (None, {'fields':('title', 'content')}),
        ('추가 옵션', {'fields': ('writer', 'likes', 'reviews'), 'classes': ('collapse',)}),
    ) # advanced options 원하는 내용으로 수정 가능
    list_per_page = 10 # 목록 페이지에 표시할 항목 수

    actions = ('increment_likes',)
    def increment_likes(self, request, queryset):
        for article in queryset:
            article.likes += 1
            article.save()
    increment_likes.short_description = '선택된 게시글의 좋아요 수 증가'