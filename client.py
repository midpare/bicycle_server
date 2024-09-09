import httpx

# 서버 주소
BASE_URL = "http://localhost:8000"

# POST 요청으로 데이터를 삽입하는 함수
async def create_item():
    async with httpx.AsyncClient() as client:
        payload = {
            "name": "Apple",
            "description": "A juicy red apple",
            "price": 1.99,
            "quantity": 10
        }
        response = await client.post(f"{BASE_URL}/items/", json=payload)
        if response.status_code == 200:
            print("POST 요청 성공:", response.json())
            return response.json()
        else:
            print("POST 요청 실패:", response.status_code)

# PUT 요청으로 데이터를 업데이트하는 함수
async def update_item(item_id: str):
    async with httpx.AsyncClient() as client:
        payload = {
            "name": "Orange",
            "description": "A sweet orange",
            "price": 2.49,
            "quantity": 20
        }
        response = await client.put(f"{BASE_URL}/items/{item_id}", json=payload)
        if response.status_code == 200:
            print("PUT 요청 성공:", response.json())
        else:
            print("PUT 요청 실패:", response.status_code)

# 아이템 조회 함수
async def get_item(item_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/items/{item_id}")
        if response.status_code == 200:
            print("GET 요청 성공:", response.json())
        else:
            print("GET 요청 실패:", response.status_code)

# 클라이언트 실행
async def main():
    result = await create_item()  # 새로운 아이템 삽입

    # PUT 요청을 보내기 전에 해당 item_id를 넣어야 합니다. 
    # 아이템 ID는 MongoDB에 저장된 후 POST 응답에 있는 값을 사용합니다.
    item_id = result['id'] # MongoDB에서 얻은 item_id 값으로 변경하세요.
    await update_item(item_id)  # 기존 아이템 업데이트

    await get_item(item_id)  # 아이템 조회

# asyncio 이벤트 루프에서 실행
import asyncio
asyncio.run(main())
