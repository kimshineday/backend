# Django
Python 기반 웹 프레임워크.<br>
    웹 개블을 빠르고 효율적으로 할 수 있음. (재사용성, 빠른 개발..)  
            -> 필요한 기능들이 대부분 내장 되어있다.

##### Django와 Flask의 차이

## 프로젝트 세팅
가상환경 만들기 > [가상환경] 장고 설치 > [가상환경 > 장고] 프로젝트 생성 > 앱등록  
### 가상환경 만들기 (venv / poetry)
```zsh
# 가상환경 생성
python -m venv 가상환경이름
# 가상환경 실행
source 가상환경이름/bin/activate
```
가상환경 이름은 프로젝트 이름을 사용하는것이 좋다.  
-> 다른 프로젝트와 혼동 피하기 위함.  
보통은 숨김 폴더 형식으로 생성하는 듯. `.`사용

### Django 설치와 set
!! 가상환경 실행 상태에서 진행
```zsh
# 가상환경에서 django 설치
pip install django
# 프로젝트 생성
django-admin startproject 프로젝트이름
```
좀 더 편하게 관리하기 위해서 config, main 등으로 생성한다.
#### App 생성 및 등록
장고로 개발시 기능마다 app를 생성(및 등록)을 통해 관리한다.
```zsh
# App 생성
python manage.py startapp 앱이름
```
manage.py 있는 폴더 안에서 실행해야함.
##### 등록
프로젝트를 생성시 기본적인 개발환경들이 구축된다.  
- 프로젝트명/settings.py  
INSTALLED_APPS 리스트에 생성한 앱을 등록한다.  
```python
# settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig', # app 등록
    'articles.apps.ArticlesConfig', # app 등록
]
```
#### DB migration
기본 DB Table 생성
```zsh
python manage.py migrate
```
manage.py 있는 폴더 안에서 실행해야함.
### 개발 서버 실행
```zsh
python manage.py runserver
```
#### 브라우저
http://127.0.0.1:8000/

## URL
사용자 요청을 받아 응답을 준다.
### Uniform Resource Locator
사용자가 접속하는 웹 주소
#### urls.py
urls.py에서 관리된다.
프로젝트 폴더, 앱 폴더에 생성이 되어있다.  
보통은 앱/urls.py에서 세부적인 url를 관리하며,  
포로젝트/urls.py에서 include로 끌어온다.
##### 프로젝트이름/urls.py
-> 전체적인 Url 관리  
`path("앱이름/", include("앱이름.urls"))`
##### app이름/urls.py
-> 기능별 Url 관리  
`path("", views.사용할_정의한함수_이름)`
프로젝트/urls.py에서 iclude로 정의를 했다면,  
앱 처음 기본 페이지는 공백 `""`으로 처리.  

## VIEW
url에서 요청을 받아와 처리하는 로직들.  
이를 통해 요청을 응답한다.
### app이름/views.py
주로 DB에서 데이터를 가져오거나, HTML로 렌더링을 한다.

## MODEL
DB 생성하고 관리한다.
테이블의 구조(스키마)정의,  
데이터를 사용할 수 있게 연결.
```python
class Menu(models.Model): # DB Table 정의
    # 변수 할당, Table Calumn 생성
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='카테고리')
    food = models.CharField(max_length=2, unique=True)
```
### 관계 필드
ForeignKey > 1:N  
OneToOneField > 1:1  
ManyToManyField > M:N
### DB 적용
```zsh
python manage.py makemigrations # DB 구조의 변화가 있을 때
python manage.py migrate # DB에 적용
```
## ADMIN
데이터 관리용 웹 서비스
### 관리자 계정 생성
```zsh
# = super user 생성
python manage.py createsuperuser
```
### 모델 등록
관리할 모델을 등록해야 웹에서 관리 가능.
```python
from .models import Category # models.py에 있는 DB Import
# 관리할 모델 등록 
admin.site.register(Category)
```
### Custom
- list_display  
: 목록에 표시할 필드지정
- list_filter  
: 필터링 옵션 추가  
- search_fields<br> 
: 검색 기능 추가
- date_hierarchy<br>
: 날짜/ 시간 기준으로 탐색
- fieldsets<br>
: 입력폼 필드
```python
class Menu(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='카테고리')
    food = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.food
```
#### 또 다른 예시
```python
# blog/admin.py
from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin): # Post 모델을 위한 커스텀 관리자 클래스
    list_display = ('title', 'author', 'pub_date') # 목록에 표시할 필드
    list_filter = ('pub_date', 'author') # 발행일과 작성자로 필터링
    search_fields = ('title', 'content') # 제목과 내용으로 검색 가능
    date_hierarchy = 'pub_date' # 발행일 기준으로 계층적인 날짜 필터링

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'text', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('text',)

admin.site.register(Post, PostAdmin) # Post 모델에 PostAdmin 클래스 적용
admin.site.register(Comment, CommentAdmin) # Comment 모델에 CommentAdmin 클래스 적용
```

## ORM
### Object-Relational Mapping
DB 데이터를 파이썬에서 쿼리 없이 객체처럼 다룰 수 있게 해줌.  
-> 파이썬 코드로 DB 작업
```python
# Model.objects
모델이름.objects.all() # 모든데이터 가져오기
모델이름.objects.get() # 조건에 맞는 딱 한가지 데이터 가져오기
모델이름.objects.filter() # 조건에 맞는 여러 데이터 가져오기
모델이름.objects.create() # 데이터 생성
객체.필드 = 값; 객체.save() # 데이터 수정
객체.delete() # 데이터 삭제
```

#### 주요 Query Set 메소드
```python
# 정렬
order_by() # - 내림차순
# 객체 수
count()
# 존재 여부
exists()
## 상세 조건
__ # 언더바 두개
# Q 객체
```