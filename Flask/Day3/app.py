from flask import Flask
from flask_smorest import Api
from db import db
# from models import User, Board

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:rlaqlcskf@000@localhost/FlaskDB' # DB 정보
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 메모리 영역, 객채가 변경이 될때마다 트래킹을 할지 여부. 웬만해서 F.
# DB 연동
db.init_app(app)

# blurprint 설정
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-u1"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdlivr.net/npm/swagger-uo-dist/"

# 블루프린트 가져오기
from routes.user import user_bip
from routes.board import board_blp

api = Api(app)
# api.register_blueprint()
api.register_blueprint(user_bip)
api.register_blueprint(board_blp)

from flask import render_template
@app.route("/manage-boards")
def manage_boards():
    return render_template('boards.html')

@app.route("/manage-users")
def manage_users():
    return render_template('users.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print('실행?')
        db.create_all()
    app.run(debug=True)