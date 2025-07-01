from django.urls import path
from . import views
"""
urlpatterns = [
    # 'feeds/' 등록 했기때문에 생략.
    path("", views.show_feed), # feeds 라는 url 접근시 show_feed 함수 실행
    path("all", views.all_feed),
    path("<int:feed_id>/<str:feed_content>", views.one_feed)
]
"""

urlpatterns = [
    path('', views.Feeds.as_view(), name='all_feeds'), # 이름 지정
    path('<int:feed_id>', views.FeedDetail.as_view(), name='feed_detail'), # 이름 지정
]