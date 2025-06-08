from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from db import db
from models import Board

board_blp = Blueprint('Boards', 'boards', description='Operations on boards', url_prefix='/board')

# API List
# '/board'
# GET, 전체 게시글 가져오는 API
# POST, 게시글 작성 API
# 블루 프린트 
@board_blp.route('/')
class BoardList(MethodView):
    def get(self):
        boards = Board.query.all() # 전체 데이터 가져오기

        # for board in boards: # 데이터를 가져와 각각의 속성값에 접근
        #     print('id', board.id)
        #     print('title', board.title)
        #     print('content', board.content)
        #     print('user_id', board.user_id)
        #     # print('author', board.author) # user를 가리키고 있음.

        #     print('author_name', board.author.name) # User
        #     print('author_email', board.author.email) # User email

        return jsonify([{"id": board.id,
                        "title": board.title, 
                        "content": board.content,
                        "user_id": board.user_id,
                        "author_name": board.author.name,
                        "author_email": board.author.email} 
                        for board in boards])

    def post(self): # 새로운 게시글
        data = request.json # 유저로부터 데이터 가져옴
        new_board = Board(title=data['title'], content=data['content'], user_id=data['user_id']) # 객체 생성
        db.session.add(new_board) # 데이터 추가
        db.session.commit() # 데이터베이스에 들어가는.
        return jsonify({"msg": "Board created"}), 201

#'/board/<int: board_id>



@board_blp.route('/<int:board_id>')
class BoardResource(MethodView): # 여러개 만들땐 List, 하나 만들땐 단일로.
    def get(self, board_id): # GET, 하나의 게시글 불러오기
        board = Board.query.get_or_404(board_id) # 데이터 가져오기, 데이터가 없으면 not found
        return jsonify({"title": board.title, 
                        "content": board.content,
                        "author": board.author.name})

    def put(self, board_id): # PUT, 특정 게시글 수정 -> 업데이트
        board = Board.query.get_or_404(board_id) # 수정하고자 하는 데이터 가져오기
        data = request.json # 업데이트 할 데이터를 가져오는.
        # 덮어쓰기
        board.title = data['title'] 
        board.content = data['content']
        db.session.commit() # DB 반영
        return jsonify({"msg": "수정 완료"})

    def delete(self, board_id): # DELETE, 특정 게시글 삭제
        board = Board.query.get_or_404(board_id) # 지우고자 하는 데이터 불러오기
        db.session.delete(board) # 삭제
        db.session.commit() # DB 반영
        return jsonify({"msg": "삭제 완료"})