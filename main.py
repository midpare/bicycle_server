from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
import os

# FastAPI 앱 생성
app = FastAPI()

# MongoDB 클라이언트 연결
client = MongoClient(os.getenv("MONGODB_URI"))
db = client["bicycle"]  # 데이터베이스 선택
collection = db["info"]  # 컬렉션 선택

# Pydantic 모델 정의
class Item(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

# MongoDB에서 ObjectId를 JSON으로 변환하는 헬퍼 함수
def item_helper(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "description": item["description"],
        "price": item["price"],
        "quantity": item["quantity"]
    }

# 데이터 삽입 (POST)
@app.post("/items/")
async def create_item(item: Item):
    # MongoDB에 데이터 삽입
    inserted_item = collection.insert_one(item.model_dump())
    new_item = collection.find_one({"_id": inserted_item.inserted_id})
    return item_helper(new_item)

# 데이터 업데이트 (PUT)
@app.put("/items/{item_id}")
async def update_item(item_id: str, item: Item):
    # MongoDB에서 해당 ID의 데이터 업데이트
    updated_item = collection.find_one_and_update(
        {"_id": ObjectId(item_id)},
        {"$set": item.model_dump()},
        return_document=True
    )
    
    if updated_item:
        return item_helper(updated_item)
    else:
        raise HTTPException(status_code=404, detail="Item not found")

# 데이터 조회 (GET)
@app.get("/items/{item_id}")
async def read_item(item_id: str):
    item = collection.find_one({"_id": ObjectId(item_id)})
    if item:
        return item_helper(item)
    else:
        raise HTTPException(status_code=404, detail="Item not found")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)