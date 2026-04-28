import numpy as np

# .concatenate( (x, y), axis = 0 ), axis = 0(행기준) 1(열기준)
x = np.array( [[1, 2], [3, 4]] )
y = np.array( [[5, 6], [7, 8]] )

print( np.concatenate( (x, y), axis = 0 ) ) # x 아래로 y가 붙는다.
print( np.concatenate( (x, y), axis = 1 ) ) # x 오른쪽으로 y가 붙는다

# 정렬, .sort( x ): 오름차순 정렬
x = np.array( [ 3, 1, 2, 5, 4 ] )
print( np.sort( x ) )               # [1, 2, 3, 4, 5]
print( np.sort( x )[ : : -1 ] )     # [5, 4, 3, 2, 1]

# 2차원 정렬, .sort( x, axios = 0), axis = 0(열 기준), 1(행기준)
x = np.array( [[12, 1, 2], [9, 8, 7]] )
print( np.sort( x, axis=0 ) )       # 열 기준 오름차순
print( np.sort( x, axis=1 ) )       # 행 기준 오름차순
print( np.sort( x, axis=None ) )    # [ 1, 2, 7, 8, 9, 12 ] # 1차원 평탄화후 정렬
# 2차원 정렬 내림차순 주의할 점: 2차원 슬라이싱 사용, [ 행 슬라이싱, 열 슬라이싱 ]
print( np.sort( x, axis=0 )[:: -1 ] )
print( np.sort( x, axis=1 )[:: -1 ] )

# np.sort( ) vs 배열.sort()
x = np.array([5,1,3])
print( np.sort(x) )
print( x.sort() )
print( x )

# .lexsort( , 1차 기준), 다중 정렬, 1차 정렬 후 만약에 1차정렬에서 동일한 값이 존재하면 동일한 값끼리
x = np.array([ 20, 30, 22, 24 ] )
y = np.array([ '철수', '영희', '민수', '영희' ] )
z = np.lexsort( (x, y) )

# 필터링
x = np.array( [10,20,30,40,50])
print( x > 30 )
print( x[ x > 30 ] )

y = np.array([[1,2,3],[4,5,6],[7,8,9]])
print( y % 2 == 0)
print( y[y%2==0])

# 조건부 필터링, .where( 조건, 참, 거짓 )
print( np.where( x > 30, x , 0) )
print( np.where( y%2==0, y, 1) )

# 마스크 필터링
con1 = x > 30
z = np.ma.array(x, mask=con1)
print( np.ma.sum( z ) )

# 다수 조건 필터링
con2 = y % 2 == 0
con3 = y % 4 == 0

print( y[con2 & con3] )     # & : 이면서
print( y[con2 | con3] )     # | : 이거나
print( y[~con2] )           # ~: 부정

# 특정 조건 충족하는 배열 반환, .extract( 조건, x ): 조건을 충족하는 요소만 추출
print( np.extract( y % 2 == 0, y ) )