import pandas as pd
# pd.Series # 1차원
# pd.DataFrame # 2차원

# [1] 데이터프레임 생성
data_list = [ ['ant', 25, 'seoul'], 
             ['bee', '30', 'busan'], 
             ['cat', 35, 'incheon']]

x = pd.DataFrame( data_list, columns=['name', 'age', 'city'] )
print( x )

# [2] 데이터프레임 생성2, 딕셔너리, 열 이름 생략 가능
data_dict = { 'name' : ['ant', 'bee', 'cat'], 
             'age' : [25, 30, 35], 
             'city' : ['seoul', 'busan', 'incheon']}
x = pd.DataFrame( data_dict )
print( x )

# [3] 데이터프레임 생성3, pd.DataFrame( 넘파이배열, colums = [ 열이름 ] )
import numpy as np
data_np = np.array( data_list )
x = pd.DataFrame( data_np, columns=['name', 'age', 'city'], index=['a', 'b', 'c'])
print( x )

# [4] 주요 속성
print( x.shape )    # (3, 3) 핼/열 크기
print( x.columns )  # 컬럼(열) 목록
print( x.index )    # 인덱스(행) 목록
print( x.values)    # 값만 2차원으로 반환

# [5] 주요 탐색
print( x.head(2) )  # 상위n개만 반환
print( x.tail(2) )  # 하위n개만 반환
x.info()            # 전처리(데이터 정리) 하기전 결측치/타입 *확인*

# [6] 인덱싱
print( x.iloc[1] )  # iloc[인덱스번호]
print( x.iloc[1, 2])    # iloc[행번호, 열번호]
print( x.loc['b'])  # loc[라벨명]
print( x.loc['b', 'city'])  #[ 라벨명, 컬럼명 ]

# [7] 슬라이싱, [시작인덱스 : 끝인덱스], [시작라벨명, 끝라벨명]
print( x.iloc[ 0:2, 0:1 ] ) # [행슬라이싱, 열슬라이싱]
print( x.loc['a':'b', 'name':'city'])

# [8] 새로운 열 추가, ['새로운열'] = 새로운값, .assign( 새로운열 = 새로운값 )
x['score'] = [100, 80, 95]  # 파괴적( 원본 수정 )
print( x )

x = x.assign( score2 = [87, 65, 78] ) # 비파괴적(새로운 pandas 반환)
print( x )

# [9] 특정한 값 수정
x['age'] = [ 31, 52, 40 ]
print( x )

x.loc[ 'b', 'age' ] = 70 # b행의 age열 값을 70으로 수정
print( x )

x.iloc[ 0, 0 ] = 'apple' # 0행의 0열의 값을 'apple'로 변경/수정
print( x )

# 여러개 한 번에 수정
# loc[ 시작라벨 : 끝라벨, 컬럼라벨] = [새로운값]
# iloc[ 시작인덱스, 끝인덱스], 수정컬럼인덱스] = [새로운값]
x.loc[ ['a', 'b'], 'score' ] = [ 10, 20 ]
print( x )

# [10] 필터링, x[ 조건식 ], x[ x[열이름] > y ]
cont1 = x[ 'score2' ] > 70
print( cont1 )      # True, False, True
print( x[ cont1 ] ) # 데이터프레임[조건]

cont2 = x['age'] > 35   # 2번째 조건
print( x[ cont1 & cont2 ] )
print( x[ cont1 | cont2 ] )

# [11] 필터링 조건으로 새로운 열 추가 또는 수정 가능.
x.loc[ x['score2'] > 70, 'passed'] = True
x.loc[ x['score2'] <= 70, 'passed'] = False
print( x )

# [12] 열(컬럼) 이름 수정, .rename( index={}, columns={'old' : 'new'} )
x = x.rename( columns={'city':'도시', 'age':'나이'})

# [13]집계 , .describe() : 수치자료들을 집계 요약
print( x.describe() )

print( x['나이'].sum() )    #[열이름].집계함수()
print( x['score'].mean() )
print( x['passed'].value_counts() ) # 특정 열의 빈도 확인