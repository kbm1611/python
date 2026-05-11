import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

# [1] 크롤링 주소 확인:
url = "https://www.yes24.com/product/category/bestseller?categoryNumber=001"

book_list = []
# [2] 주소의 매개변수 분석, categoryNumber=001&pageNumber=1*pagerSize=24&sex=M&age=30&goodsStatGb=03
# 1~3 페이지 크롤링 예
for page in range( 1, 4 ) :
    url = f'https://www.yes24.com/product/category/bestseller?pageNumber={page}'
    # [3] url 요청
    response = requests.get( url )
    # [4] 요청한 url 요청이 성공했을 때 html로 파싱
    soup = BeautifulSoup( response.text, "html.parser" )
    # [5] 가져올 식별자, soup.select() : 여러개 선택, soup.seelect_one() 하나선택
    books = soup.select( '#yesBestList > li' )
    # 책하나당 : ( .gd_name 제목, .yes_b 가격, info_auth 저자 정보 )
    for book in books: # <li> 여러개이므로 반복문 가능
        gd_name = book.select_one('.gd_name').get_text().strip()
        yes_b = book.select_one('.yes_b').get_text().strip()
        info_auth = book.select_one('.info_auth').get_text().strip()
        # [6] 리스트[]에 딕셔너리{} 포함하기
        book_list.append( { "제목" : gd_name, "가격" : yes_b, "저자정보" : info_auth } )
        # [7] import time , time.sleep( 초 ), 지정한 초만큼 코드(스레드)가 멈춘다.
        time.sleep( 2 )

# [8] 판다스에 넣어주기
print( book_list )
df = pd.DataFrame( book_list )
print( df )