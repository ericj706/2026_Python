# 1. import
from fastapi import FastAPI
import uvicorn
# 2. fastapi 객체 생성
app = FastAPI()
# 3. 서버실행 함수
if __name__ == "__main__" :
    uvicorn.run("f-02:app", host="127.0.0.1",port=8000,reload=True)
# 4. 서버 실행 : 현재파일 py 실행 , 여러번 실행 불가능 
# http://127.0.0.1:8000/docs
# 5. HTTP REST 구현 , REST : 
# 1) FASTAPI 객체 내 get/post/put/delete 메소드 지원
@app.get("/") # @app.get("/매핑주소")
async def index() : # async def 함수명() : 비동기 함수 선언
    return "안녕 파이썬 웹" # 반환값
# 코드 작성 후 서버 재실행 없이 "reload=True" 속성 적용 -> 서버에 계속 자동반영
# 2) 쿼리스트링 : HTTP URL 경로상에 ? 뒤로 정의된 변수들
@app.get("/user")
async def user(name, age:int) : # 파이썬은 동적 타입이지만 "변수명.타입명" 정적 타입 가능
    info = {'name':name , 'age':age , 'msg':'*쿼리통신 성공*'}
    return info # 딕셔너리가 JSOn 타입으로 자동 반환
# 3) 경로 파라미터: HTTP URL 경로 상에 / 구분하여 변수들
@app.get("/item/{name}/{age}") # /item/유재석/40 -> /item/{변수명}/{변수명}
async def item(name:str , age:int  | None=None ) :
    return {name:name,age:age,'msg' : "*경로통신 성공*"}
# 4) 본문 , HTTP GET/DELETE => 쿼리/경로 , HTTP POST/PUT => 쿼리/경로/본문 BODY
@app.post("/products")
async def products(product:dict) : # 전달받은 body본문(json) 값을 파이썬 dict타입으로 매핑
    product['msg'] = "*본문통신 성공*"
    return product
# 요청/테스트에서 body(본문)에 {"name":"유재석","age":40}으로 보내보기
