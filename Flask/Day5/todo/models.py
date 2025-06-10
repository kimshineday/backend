# models.py
from db import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    # 사용자 모델 정의
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db, String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(120))

    def set_password(self, password): # 비밀번호 해쉬화
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Todo(db.Model):
    # Todo 모델 정의
    id = db.Column(db.Integer, primay_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id), nullable=False'))