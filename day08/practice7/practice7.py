# [ Python Practice7 종합예제]

# 경기도 아파트 실거래가 조회 시스템 ( 리스트와 딕셔너리 사용 )
# 데이터 출처: 국토교통부 실거래가 공개시스템(경기도 최근 1년치 아파트 매매 데이터) 
# https://rt.molit.go.kr/pt/xls/xls.do?mobileAt=

# 주요 기능 요구사항
# 1. 데이터 저장 및 로드 (파일 처리)
#     users.txt: 회원 정보 저장 (식별번호,아이디,비밀번호,이름) 직접 생성 
#     아파트(매매)_실거래가_20260424091956.csv: 직접 다운로드한 실거래가 데이터 파일

# 2. 사용자 기능 (로그인 후 이용 가능)
#     2-1) 공통 : 
#       - 회원가입, 
#       - 로그인
#       - 로그아웃
#     2-2) 회원 전용 메뉴: ( 어려운분들은 구현 안해도 됩니다. )
#       - 지역명 검색: '시군구' 열에서 사용자가 입력한 지역명(예: "만안구", "평촌동")이 포함된 모든 거래 내역 출력
#       - 금액 범위 검색: 사용자가 입력한 '최소 금액'과 '최대 금액' 사이의 거래 내역 필터링 출력
#       - 전체 통계 조회: 전체 데이터의 평균 거래가 등 간단한 통계 정보 출력

# 정보 인덱스 확인
# ['158711',                    No 0
# '경기도 부천시 원미구 상동',  시군구 1 -> 지역명검색에 사용
# '525-1',                      번지 2
# '0525',                       본번 3
# '0001',                       부번 4
# '라일락마을(경남아너스빌)',   단지명 5
# '84.8000',                    전용면적 6
# '202504',                     계약년월 7
# '25',                         계약일 8
# '63,000',                     거래금액(만원) 9 -> 금액 범위 검색에 사용
# '2304',                       동 10
# '2',                          층 11
# '개인',                       매수자 12
#  '개인',                      매도자 13
#  '2002',                      건축년도 14
# '도약로 16',                  도로명 15
# '-',                          해제사유발생일 16
# '중개거래',                   거래유형 17
# '경기 부천시 원미구',         중개사소재지 18
# '25.08.13']                   등기일자 19

import csv

def signup(uno, uid, upw):

    with open("./day08/practice7/user.txt", 'a') as file:
        file.write(f"{uno},{uid},{upw}\n")
    
    return True

def get_userList():
    userList = {}
    try:
       with open("./day08/practice7/user.txt", "r") as file:
        for line in file:
            uno, uid, upw = line.strip().split(',')
            userList[uid] = upw
    except:
        print("파일 열기에 실패하였습니다.")
    
    return userList

def get_lastUno():
    lastUno = 0
    try:
        with open("./day08/practice7/user.txt", "r") as file:
            lines = file.readlines()
        
            if lines:
                last_line = lines[-1]
                lastUno = int(last_line.split(',')[0])
            else:
                return 0
    except:
        print("파일 열기에 실패하였습니다.")
        return 0
    

def login(userList, uid, upw):
    if uid in userList and userList[uid] == upw:
        return True
    else:
        return False

def userMenu():
    while True:
        print()
        print("1.지역명 검색|2.금액 범위 검색|3.전체 통계 조회|4.로그아웃")
        ch = int( input('선택>') )

        #지역명 검색
        if(ch == 1):
            count = 0 #검색된 개수 세는 변수
            location = input("지역명 입력>")
            with open("./day08/practice7/data.csv", "r", encoding='cp949') as file:
                reader = csv.reader(file)

                # 헤더 건너뛰기
                for i in range(16):
                    next(reader)

                print("--- 검색 결과 ---")
                for row in reader:
                    if location in row[1]:
                        print(row)
                        count += 1
                print(f"검색된 개수:", count)

        #금액 범위 검색
        elif( ch == 2 ):
            count = 0 #검색된 개수 세는 변수
            minPrice = int(input("최소 금액 입력(단위: 만원)>"))
            maxPrice = int(input("최대 금액 입력(단위: 만원)>"))
            with open("./day08/practice7/data.csv", "r", encoding='cp949') as file:
                reader = csv.reader(file)

                # 헤더 건너뛰기
                for i in range(16):
                    next(reader)

                print("--- 검색 결과 ---")
                for row in reader:
                    price = int(row[9].replace(',', ''))  # 거래금액에서 쉼표 제거 후 정수로 변환
                    if minPrice <= price <= maxPrice:
                        print(row)
                        count += 1
                print(f"검색된 개수:", count)

        # 전체 통계 조회
        # 1.전체 평균 거래가
        # 2.평균 거래가가 가장 높은 경기도의 3개의 시
        # 3.월별 거래회수
        elif( ch == 3 ):
            priceCnt = 0 # 금액이 들어있는 row 세기
            averagePrice = 0 # 총 평균 금액
            cityPrice = {} # 시끼리 묶어서 가장 상위 3개의 도시 출력
            monthCount = {} # 월별 통계량 출력
            with open("./day08/practice7/data.csv", "r", encoding='cp949') as file:
                reader = csv.reader(file)

                # 헤더 건너뛰기
                for i in range(16):
                    next(reader)

                for row in reader:
                    price = int(row[9].replace(',', ''))

                    if price == None or price == '':
                        continue;
                    
                    priceCnt += 1
                    averagePrice += price
                    

                    city = row[1].split()[1]
                    if city not in cityPrice:
                        cityPrice[city] = price
                    else:
                        cityPrice[city] += price

                    month = row[7]
                    if month not in monthCount:
                        monthCount[month] = 1
                    else:
                        monthCount[month] += 1

                averagePrice //= priceCnt # 전체 수로 나누기
                sorted_cityPrice = dict(sorted(cityPrice.items(), key= lambda x : x[1], reverse=True)[:3]) # 금액순으로 정렬, 상위 3개만
                sorted_monthCount = dict(sorted(monthCount.items())) # 월별 정렬

                print("정렬:", sorted_cityPrice)

                print("--- 전체 통계 ---")
                print(f"1.전체 거래 평균 금액: {averagePrice}만원\n")

                print("2.거래 금액량 높은 도시 Top3")
                for i, (city, price) in enumerate(sorted_cityPrice.items()):
                    if price > 10 ** 8:
                        jo = price // ( 10 ** 8 )
                        price %= 10 ** 8
                        if price > 10 ** 4:
                            eok = price // ( 10 ** 4 )
                            price %= 10 ** 4
                            print(f"-{i+1}번째 거래금액 높은 도시: {city}({jo}조{eok}억{price}만원)")
                        else:
                            print(f"-{i+1}번째 거래금액 높은 도시: {city}({jo}조{price}만원)")
                    else:
                        if price > 10 ** 4:
                            eok = price // ( 10 ** 4 )
                            price %= 10 ** 4
                            print(f"-{i+1}번째 거래금액 높은 도시: {city}({eok}억{price}만원)")
                        else:
                            print(f"-{i+1}번째 거래금액 높은 도시: {city}({price}만원)")
                print()

                print("3.월별 거래량")
                for month in sorted_monthCount:
                    print(f"-{month[:4]}년{month[4:]}월: {sorted_monthCount[month]}회")


                
        # 로그아웃
        elif( ch == 4 ):
            print("로그아웃 되었습니다.")
            break;
        else:
            print("유효하지 않는 숫자")

print("--경기도 아파트 실거래가 조회 시스템--")

# print("테스트 csv 파일")
# with open("./day08/practice7/data.csv", "r", encoding='cp949') as file:
#     reader = csv.reader(file)

#     for i in range(15):
#         next(reader)
#     header = next(reader)
        
# print("--- CSV 헤더 정보 ---")
# print(header)

while True:
    print('1.회원가입|2.로그인|3.종료')
    ch = int(input('선택>'))

    if(ch == 1):
        uno = get_lastUno() + 1
        uid = input('가입할 아이디:')
        upw = input('가입할 패스워드:')

        if( signup(uno, uid, upw) ):
            print("회원가입에 성공하셨습니다.")
        else:
            print("회원가입에 실패하셨습니다.")
    elif(ch == 2):
        uid = input('아이디:')
        upw = input('패스워드:')

        userList = get_userList()

        if( login(userList, uid, upw) ):
            print("로그인에 성공하셨습니다.")
            userMenu()
        else:
            print("로그인에 실패하셨습니다.")
    elif(ch == 3):
        break;
