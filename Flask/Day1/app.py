from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [ # 사용자 데이터
        {'username':'traveler', 'name':'Alex'},
        {'username':'photographer', 'name':'Sam'},
        {'username':'gourmet', 'name':'Chris'}
    ]
    # HTML로 데이터 보내기
    return render_template('index.html',users=users)

# 이 파일(app.py)가 직접 실행 되었을 때 웹 서버 실행
if __name__ == '__main__':
    app.run(debug=True) # 서버를 껐다 켜지 않아도 새로고침으로 변경사항 확인 가능
