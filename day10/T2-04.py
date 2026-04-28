import numpy as np

# 배열 연산, 두 배열간의 동일한 위치끼리 연산 진행
x = np.array( [1, 2, 3] )
y = np.array( [4, 5, 6] )
print( x + y )
print( x - y )
print( x * y )
print( x / y )
print( x % y )
print( x ** y )

# 비교 연산
print( x > y )
print( x == y )

# 배열 + 숫자: 자동으로 전체에 적용
print( x + 10 ) # [11 12 13]
print( y * 2 )  # [8 10 12]

# 논리 연산
x = np.array( [ True, False, True ] )
y = np.array( [ False, False, True ] )
print( np.logical_and( x, y ) )     # [False False True] 둘 다 참이면 참
print( np.logical_or( x, y ) )      # [True False True]
print( np.logical_not( x ) )     # [False  True False]
print( np.logical_xor( x, y ) )     # [True False False]

#루트( 수학 ), sqrt
y = np.array( [ 1, 4, 9 ] )
print( np.sqrt( y ) )       # 실수로 반환

# 2차원 비교
y = np.array( [ [1,2,3], [4,20,6] ] )
print( y > 3 )

x = np.array( [1, 10, 3] )
print( x > y)

# .all( x ): 모두가 참이면 참, .any( x ): 하나라도 참이면 참
x = np.array( [ True, False, True ])
print( np.all( x ) )
print( np.any( x ) )

# .array_equal( x, y ): 두 배열의 요소들이 모두 같으면 True, False 반환
x = np.array( [1, 2, 3] )
y = np.array( [1, 2, 3] )
z = np.array( [1, 2, 4] )
print( np.array_equal( x, y ) ) # True
print( np.array_equal( x, z ) )
