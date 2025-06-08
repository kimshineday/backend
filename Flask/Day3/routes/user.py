from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from db import db
from models import User

user_blp = Blueprint('Users', 'users', description='Operations on users', url_prefix='/user')

# API List :
@user_blp.route('/')
class UserList(MethodView): # 상속
    def get(self): # GET, 전체 유저 데이터 조회
        users = User.query.all() # 유저데이터 전부 가져오기
        # for문 대신 한줄로
        data = [{"id":user.id, 
                    "name": user.name, 
                    "email": user.email} 
                    for user in users]  # Convert to list
        return jsonify(data)

    def post(self): # POST, 유저 생성
        print("요청은 오는가?")
        data = request.json
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"msg": "계정 생성 완료"}), 201

@user_blp.route('/<int:user_id>')
class UserResource(MethodView):
    def get(self, user_id): # GET, 특정 유저 데이터 조회
        user = User.query.get_or_404(user_id)
        # print(type(user)) # Query Set
        return {"name": user.name, 'email': user.email}

    def put(self, user_id): # PUT, 특정 유저 데이터 업데이트
        user = User.query.get_or_404(user_id)
        data = request.json # 수정할 데이터
        # 덮어쓰기
        user.name = data['name']
        user.email = data['email']
        
        db.session.commit() # DB 반영
        return {"msg": "수정 완료"}

    def delete(self, user_id): # DELETE, 특정 유저 삭제
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"msg": "계정 삭제 완료"}