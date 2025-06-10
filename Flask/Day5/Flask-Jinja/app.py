from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 임시 사용자 데이터
users = [
    {"username": "traveler", "name": "Alex"},
    {"username": "photographer", "name": "Sam"},
    {"username": "gourmet", "name": "Chris"}
]

@app.route('/')
def index():
    return render_template('index.html', users=users)

# 사용자 추가, 수정, 삭제 라우트 및 함수 작성...
@app.route('/add', methods=['GET', 'POST']) # 사용자 추가하는 라우트
def add():
    if request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        users.append({'username': username, 'name': name})
        return redirect(url_for('index'))
    return render_template('add_user.html')

@app.route('/edit/<username>', methods=['GET', 'POST']) # 수정하는 라우트
def edit():
    user = next((user for user in users if user['username'] == username), None)
    if not user:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        user['name'] = request.form['name']
        return redirect(url_for('index'))

    return render_template('edit_user.html, user=user')

@app.route('/delete/<username>') # 삭제하는 라우트
def delete():
    global users
    users = [user for user in users if user['username'] != username]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)