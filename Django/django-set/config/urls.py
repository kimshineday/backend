"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from feeds import views # feeds 불러오기

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("feeds/", views.show_feed), # feeds 라는 url 접근시 show_feed 함수 실행
    # path("feeds/all", views.all_feed),
    # path("feeds/<int:feed_id>/<str:feed_content>", views.one_feed)
    
    # -> 내용이 많아지면서 관리가 어려워짐. 중복 되는 부분을 묶어주는 것.
    # path("feeds/", include("feeds.urls")) # feeds 등록
    
    # API 코드 제작
    path('api/v1/feeds/', include('feeds.urls')),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/reviews', include('reviews.urls'))
]
# 잘못된 접근을 막아줄 수 있는.