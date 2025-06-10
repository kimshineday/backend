# app.py
from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from flask_smorest import Api

from db import db
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db" # 로컬 DB 파일 형태의 간단한 데이터베이스
app.config["JWT_SECRET_KEY"] = "super-secret-key"

# db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)
api = Api(app)

# 모델 및 리소스 불러오기
from models import User, Todo
from routes.auth import auth_blp
from routes.todo import todo_blp

# API에 블루프린트 
api.register_blueprint(auth_blp)
api.register_blueprint(todo_blp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)