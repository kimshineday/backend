# API CRUD 작업
from flask import request, jsonify
from flask_smorest import Blueprint, abort

def create_posts_blueprint(mysql):
    posts_blp = Blueprint('posts', __name__, description='posts api', url_prefix='/posts')

    @posts_blp.route('/', methods=['GET', 'POST'])
    def posts():
        cursor = mysql.connection.cursor()
        if request.method == 'GET': # 게시글 조회
            sql = 'SELECT * FROM posts'
            cursor.execute(sql)

            posts = cursor.fetchall() # 전체데이터 가져오기
            cursor.close()

            post_list = []
            for post in posts:
                post_list.append({
                    'id': post[0],
                    'title': post[1],
                    'content': post[2],
                })
            return jsonify(post_list)
        # 게시글 생성
        if request.method == 'POST':
            title = request.json.get('title')
            content = request.json.get('content')

            if not title or not content:
                abort(400, message='제목과 내용을 입력해주세요')

            sql = "INSERT INTO posts(title, content) VALUES(%s, %s)"
            cursor.execute(sql, (title, content))
            mysql.connection.commit()

            return jsonify({'msg': '성공적으로 포스팅 되었습니다.'}), 201

    # 게시글 조회
    # 게시글 수정 및 삭제
    @posts_blp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def post(id):
        cursor = mysql.connection.cursor()
        if request.method == 'GET':
            sql = 'SELECT * FROM posts WHERE id = %s'
            cursor.execute(sql)
            post = cursor.fetchone()

            if not post:
                abort(404, message='글을 찾을 수 없습니다.')
            return ({
                'id': post[0],
                'title': post[1],
                'content': post[2],
            })
        elif request.method == 'PUT':
            # 데이터 가져오기
            title = request.json.get('title') # title = request.json
            content = request.json.get('content') # content = data('title')
            if not title or not content or not post:
                abort(404, '게시글이 없습니다.')
            sql = "UPDATE posts SET title = {title}, content = {content} WHERE id = {id}"
            cursor.execute(sql)
            mysql.connection.commit()

            return jsonify({'msg': '성공적으로 저장되었습니다.'}), 200

        elif request.method == 'DELETE':
            if not post:
                abort(404, '게시글이 없습니다.')
            sql = "DELETE FROM posts WHERE id = {id}"
            cursor.execute(sql)
            mysql.connection.commit()

            return jsonify({'msg': '게시글이 삭제되었습니다.'})

    return posts_blp
