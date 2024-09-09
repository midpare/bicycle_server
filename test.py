from pymongo import MongoClient

# MongoDB에 연결
client = MongoClient("mongodb+srv://midpare:moMinjun132!@cluster0.ty8un.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# "mydatabase"라는 데이터베이스 선택 (없으면 자동으로 생성됨)
db = client["bicycle"]

# "mycollection"이라는 컬렉션 선택 (없으면 자동으로 생성됨)
collection = db["info"]
collection.delete_one({"name": "Alice"})