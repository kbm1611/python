# numpy: 배열 기반, 공학 수치 계산
# pandas: 테이블 기반, 전처리/필터링(numpy)

# [1] pandas 설치: pip install pandas
# [2] import pandas as pd

import pandas as pd
print( pd.__version__) # 3.0.2

# series
# 1. 생성
x = [ 10, 20, 30, 40, 50 ]
z = pd.Series( x )
print( z )

# 2. 각 요소들으 라벨 포함하기
y = [ 'a', 'b', 'c', 'd', 'e' ]
z = pd.Series( x, index = y )
print( z )

# 3. 딕셔너리로 생성
# 파이썬 주요 타입
x = { 'apple' : 1, 'banana' : 2, 'cherry' : 3 }
z = pd.Series( x )
print( z )

# 4. 주요 속성 확인
print('--4--')
print( z.dtype )    # 타입반환, int64
print( z.index )    # 인덱스반환, Index(['apple', 'banana', 'cherry'], dtype='str')
print( z.values )   # 값반환, [1, 2, 3]
print( z.head(2) )  # .head(n), 상위 n개(기본값:5)만 출력(확인용)
print( z.tail(2) )  # .tail(n), 하위 n개만 출력

# 5. 인덱싱
print( z.iloc[0] )                  # .iloc[인덱스번호], 라벨이 아닌 위치로 조회
print( z.loc['apple'])              # loc[ 라벨명 ], 라벨명으로 조회
print( z.loc['apple' : 'cherry'])   # loc[ 시작라벨 : 끝라벨 ]

# 6. 데이터 수정
z['apple'] = 10     # [ 기존라벨명 ] = 새로운 값
print( z )
print( z['apple'] ) # [ 기존라벨명 ]

# 7. 데이터 추가
z[ 'berry' ] = 40   # [ 새로운라벨명 ] = 새로운값
print( z )

# 8. 병합 , .concat( [ x , y ] )
# 파이썬 리스트 합치기
x = [10, 20, 30]
y = [40, 50]
print( x + y )
print( [ x + y ] )
print( [ *x, *y ] )

# pandas
x = pd.Series( [10, 20, 30], index=['a', 'b', 'c'] )
y = pd.Series( [40, 50], index=['d', 'e'] )
z = pd.concat( [ x, y ] )
print( z )

# 9. 라벨 이름 변경 ,.rename( { '기존' : '새로운' } )
# 파이썬

z = z.rename( { 'a' : 'apple' } )
print( z )

# 10. 필터링 , [ 필터링 ]
print( z[ z > 30 ] )
x = z[ z > 30 ]
print( x )
x = z[ ( z < 25 ) | ( z > 35 ) ]
print( x )
x = z[ ( z > 25 ) | ( z < 35 ) ]
print( x )
z[ z > 30 ] = z [ z > 30 ] + 10
print( z )

# 11. 통계
print( z.sum() ) # 합계
print( z.mean() ) # 평균
print( z.max() ) # 최댓값
print( z.min() ) # 최솟값
print( z.median() ) # 중앙값
print( z.var() ) # 분산
print( z.std() ) # 표준편차
print( z.count() ) # 요소 개수
print( z.value_counts( ) ) # 각 요소별 중복 개수
print( z.value_counts( normalize=True ) ) # 각 요소가 전체에서 차지하는 비율(0~1)

# 12. 정렬, .sort_index() , .sort_values()
x = z.sort_index()      # 인덱스(라벨) 기준의 정렬
print( x )
x = z.sort_values()     # 값 기준의 정렬
print( x )

x = z.sort_index( ascending = False )   # ascending = False -> descending 내림차순
print( x )

# 13. 그룹
# .groupby( level = 0 ).집계함수(), 그룹 이후에 집계중요!
# .groupby( level = 0 ).agg( ['함수명', '함수명' ] )
z = pd.Series( [10, 20, 30, 10, 20, 30], index= ['a','b','a','b','a','b'])

x = z.groupby( level = 0 ).sum()    # 인덱스(라벨)별 총합계
print( x )

x = z.groupby( level = 0 ).mean()
print( x )

x = z.groupby( level = 0 ).agg(['sum', 'mean', 'count'])    # 여러개 집계함수는 agg 함수로 묶어서 표현
print(x)