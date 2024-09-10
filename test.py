from pymongo import MongoClient
import os

# MongoDB에 연결
client = MongoClient(os.getenv("MONGODB_URI"))

# "mydatabase"라는 데이터베이스 선택 (없으면 자동으로 생성됨)
db = client["bicycle"]

# "mycollection"이라는 컬렉션 선택 (없으면 자동으로 생성됨)
collection = db["info"]
result = collection.find_one({"name": "Apple"})
print(result)