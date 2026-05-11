
# 동적페이지 크롤링
# - 웹페이지 자료가 대기 상태 / 이벤트가 있는 경우

# [1] 설치
# pip install playwright    # 파이썬 라이브러리
# playwright install        # 현재 PC에 설치

# [2] 라이브러리
import asyncio # 비동기 라이브러리
from playwright.async_api import async_playwright # 동적페이지 크롤링 라이브러리
import pandas as pd

# 크롤링 주소
# 주소 "https://search.naver.com/search.naver?where=image&query=짱구"
# 박스 : title_item , 이미지 : _fe_image_tab_content_thumbnail_image, 제목 : info_title

# [4] 동기 웹 크롤링
async def naverRun() : # 동기화된 함수
    # (1) playwright 실행하고 p 변수에 결과 대입
    async with async_playwright() as p: #
        # (2) awiat(대기) 상태 이용한 크롬 실행
        # headless = False : 브라우저가 직접 실행된다. <봇차단 방지>
        browser = await p.chromium.launch( headless=False )
        
        # (3)
        url = "https://search.naver.com/search.naver?where=image&query=짱구"
        page = await browser.new_page()
        await page.goto( url )
        
        # (4-1) (자료가 표시될 때까지 기다리기) 대기상태 만들기
        # (4-2) 스크롤 내리기 이벤트(JS)
        for i in range( 2 ):
            #시스템(인터넷속도)에 따라 적절하게 지정
            await page.wait_for_timeout( 3000 )
            # window(브라우저).scrollTo(시작위치, 이동위치)
            # 이동위치 : document(현재HTML).body(본문).scrollHeight(스크롤높이) : 즉 현재 브라우저 스크롤을 본문의 가장 하단으로 이동
            await page.evaluate("window.scrollTo( 0, document.body.scrollHeight)") # await page.evalute("JS코드")
        
        # (5) 실행된 페이지에서 특정한 요소 가져오기
        # page.query_selector_all( 식별자 ) 여러개, page.query_selector( 식별자 ) 하나
        items = await page.query_selector_all( '.tile_item' )
        image_list = []
        for item in items:
            title_tag = await item.query_selector( '.info_title .txt' )
            image_title = await title_tag.inner_text() if title_tag else '제목없음'
            
            # css 선택자: #id .class 마크업
            image_tag = await item.query_selector( '._fe_image_tab_content_thumbnail_image' ) #이미지
            image_link = await image_tag.get_attribute( 'src' ) if image_tag else '이미지링크 없음'
            print( image_link )
         
            image_list.append( { "제목" : image_title, "이미지 링크" : image_link } )
       
        print(image_list)
        # (*) (직접) 안전하게 브라우저 닫기
        await browser.close()
        
asyncio.run( naverRun() ) # 동기화된 함수 실행
