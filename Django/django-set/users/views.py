from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from .serializers import MyInfoUserSerializer
from django.contrib.auth.password_validation import validate_password

# api/v1/users [POST] => 유저 생성 API
class Users(APIView):
    def get(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user)
        return Response(serializer.data)


    def post(self, request):
        # password : 검증, 해쉬화 해서 저장
        # the other : 비밀번홍 외 다른 데이터들
        password = request.data.get('password')
        serializer = MyInfoUserSerializer(data=request.data)

        try:
            validate_password(password)
        except:
            raise ParseError('Invalid password')
        
        if serializer.is_valid():
            user = serializer.save() # 새로운 유저 생성
            user.set_password(password) # 비밀번호 해쉬화
            user.save() # 데이터 저장

            serializer = MyInfoUserSerializer(user) # 유저 데이터 보내기
            return Response(serializer.data)
        else:
            raise ParseError(serializer.errors)
        
# api/v1/users/myinfo [GET, PUT]
class MyInfo(APIView):
    def get(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request): # update
        user = request.user
        serializer = MyInfoUserSerializer(user, # 업데이트 하고자하는 유저 데이터
                                            data=request.data,
                                            partial=True) # 일부 데이터만 입력해도 업데이트 가능
        if serializer.is_valid():
            user = serializer.save()
            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
