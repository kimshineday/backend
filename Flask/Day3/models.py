# 모델 = Table 만드는 것.
# 게시글 - board, 유저 - User

from db import db

class User(db.Model):
    __tablename__ = 'users' # 유저 테이블 생성

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    # 사용자가 작성한 모든 게시물들을 나타냄
    boards = db.relationship('Board', backpopulates='author', lazy='dynamic') # 역참조 활용 / lazy=dynamic 데이터베이스로부터 즉시 모든 데이터를 로딩 하지 않음.


class Board(db.Model):
    __tablename__ = 'boards' # 게시글 객체 생성

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(300))
    # 유저 아이디 저장.
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) # 게시글 작성을 누가 했는지 알기 위한.
    # 특정 게시물을 작성한 사용자를 나타냄
    author = db.relationship('User', back_populates='boards', lazy='dynamic') # 역참조 활용


