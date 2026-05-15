# 3. 라우터: 앱(서버)와 연결되는 라우터
from fastapi import APIRouter

router = APIRouter( prefix = '/api') # 공통 URL 삽입 가능

# 4. 서비스객체 호출
from service import productService

# 5. HTTP 매핑
@router.get("/products")
async def products():
    return productService.products()

# 6. 외부 API 통신
@router.get("/spring")
async def getSpring():
    return await productService.getSpring()


