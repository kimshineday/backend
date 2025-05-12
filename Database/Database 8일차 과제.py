
from pymongo import MongoClient
"""
# 데이터 삽입
def insert_data():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.local # 'local' 데이터베이스 사용

    # 책 데이터 삽입
    books = [
        {'title': 'Kafka on the Shore', 'author': 'Haruki Murakami', 'year': 2002},
        {'title': 'Norwegian Wood', 'author': 'Haruki Murakami', 'year': 1987},
        {'title': '1Q84', 'author': 'Haruki Murakami', 'year': 2009},
    ]
    db.books.insert_many(books)

    # 영화 데이터 삽입
    movies = [
        {'title': 'Inception', 'director': 'Christopher Nolan', 'year': 2010, 'rating': 8.8},
        {'title': 'Interstellar', 'director': 'Christopher Nolan', 'year': 2014, 'rating': 8.6},
        {'title': 'The Dark Knight', 'director': 'Christopher Nolan', 'year': 2008, 'rating': 9.0}
    ]
    db.movies.insert_many(movies)

    # 사용자 행동 데이터 삽입
    user_actions = [
        {'user_id': 1, 'action': 'click', 'timestamp': '2023-04-12T08:00:00Z'},
        {'user_id': 1, 'action': 'view', 'timestamp': '2023-04-12T09:00:00Z'},
        {'user_id': 2, 'action': 'click', 'timestamp': '2023-04-12T10:00:00Z'},
    ]
    db.user_actions.insert_many(user_actions)

    print('Data inserted successfully')
    client.close()

if __name__ == '__main__':
    insert_data()

"""
# 문제 1 특정장르 책 찾기
# 데이터베이스에 새로운 필드로 'genre' 책 데이터 추가, 'fantasy' 장르의 모든 책 찾기

# 책 컬렉션 조회
def bookfind():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.local
    books = db.books.find()
    for books in books:
        print(books)
#bookfind()

# 책 컬렉션에 장르 정보 추가
def insert_genre():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.local
    db.books.update_one(
        {'title': 'Kafka on the Shore'},
        {'$set': {'genre': 'Magical realism'}}
    )
    db.books.update_one(
        {'title': 'Norwegian Wood'},
        {'$set': {'genre': 'Romance'}}
    )
    db.books.update_one(
        {'title': '1Q84'},
        {'$set': {'genre': 'Fantasy'}}
    )
#insert_genre()

# Fantasy 장르의 책 조회
def find_fantasy():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.local
    fantasy = {'genre': 'Fantasy'}
    for books in db.books.find(fantasy):
        print(books)
#find_fantasy()

# 문제 2 감독별 평균 영화 평점 계산
# 각 영화 감독별로 영화 평점평균을 계산
def movie_score():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.local
    dir_christopher = {'director': 'Christopher Nolan'}
    ratings = []
    for movie in db.movies.find(dir_christopher):
        christopher_mov = dict(movie)
        ratings.append(christopher_mov['rating'])
    avg_rating = sum(ratings) / len(ratings)
    return avg_rating
christopher = movie_score()
a = 5.22
b = 6

# 정렬
def ranking(*args):
    sorted_score = sorted(args, reverse=True)
    print(sorted_score)
#ranking(christopher, a, b)

# 문제 3 특정 사용자의 최근 행동 조회
# 최신 순으로 5개의 행동 정렬
def user_act(target):
    client = MongoClient('mongodb://localhost:27017/')
    db = client.local
    user_act = {'user_id': target}
    user_actions = db.user_actions.find(user_act).sort('timestamp', -1).limit(5)
    for user_actions in user_actions:
        print(user_actions)
#user_act(1)

# 문제 4 출판 연도별 책의 수 계산
def book_year():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.local
    books_group = db.books
    pipeline = [
        {"$group": {"_id": "$year", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]
    results = books_group.aggregate(pipeline)
    for result in results:
        print(result)
#book_year()

# 문제 5 특정 사용자 행동 유형 업데이트
# 2023.04.10 이전 view 행동을 > seen으로 변경
from datetime import datetime # datetime 이용해 기준점을 비교
def act_update():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.local
    # 기준
    target = datetime.strptime('2023-04-10T00:00:00Z', '%Y-%m-%dT%H:%M:%SZ')
    query = {
        'timestamp': {'$lt': target},
        'action': 'view'
    }
    update = {
        '$set': {'action': 'seen'}
    }
    db.user_actions.update_many(query, update)
act_update()