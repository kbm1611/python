
# 모듈 호출 하기
# 표준 모듈: 파이썬 내장 라이브러리
# 외부 모듈: 설치형 라이브러리
#import 모듈명
# 특정한변수/함수가져오기   : from 모듈명 import 가져오고 싶은 함수 또는 변수
# 모두 가져오기           : from 모듈명 import *
# 식별자부여              : from 모듈명 as 식별자명

print("-----math------")
import math             # import 모듈명
print( math.sin(1) )    # 호출한 모듈에서 sin 함수 호출, .(접근 연산자)
print( math.cos(1) )
print( math.tan(1) )
print( math.floor(2.5) )
print( math.ceil(2.5) )

from math import sin, cos, tan, floor, ceil

import math as m
print( m.sin(1) )

# random 모듈
import random
print("\n-----random------")

print( random.random() ) # 0.0 ~ 1.0 사이의 난수 생성
print( random.uniform(19.99999999999999, 20) ) # uniform( 시작값, 끝값 ) 지정된 범위 사이의 난수(실수) 생성
print( random.randrange(1, 10) )        #randrange(시작값, 끝값) 지정된 범위 사이의 정수 반환
print( random.choice( [10, 24, 5, 20] )) #choice( [리스트] ) . 리스트내 랜덤 요소 1개 반환
a = [1,2,3,4,5]
random.shuffle( a )
print( a ) #shuffle( [리스트] ) , 리스트내 요소들을 랜덤으로 섞는다.
print( random.sample( [1,2,3,4,5], k = 2 ) ) # sample( [리스트], k = 개수 ), 리스트내 k개 랜덤 요소 반환
# k=2 : 키워드 매개변수 , k라는 이름을 갖는 매개변수에 대입


import sys
print(sys.argv)
print("---")

print("getwindowsversion:()", sys.getwindowsversion())
print("---")
print("copyright:", sys.copyright)
print("---")
print("version:", sys.version)

sys.exit()