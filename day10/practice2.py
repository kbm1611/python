import numpy as np
# 문제 1: 기본 인덱싱
x = np.array([10,20,30,40,50])
print( x[3] )
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
print( x[1,2] )

# 문제 2: 음수 인덱싱
x = np.array([10,20,30,40,50])
print( x[-1] )
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
print( x[-1, -1])

# 문제 3: 불리언 & 팬시 인덱싱
x = np.array([10,20,30,40,50])
y = x > 30
print( x[y] )
print( x[ [ 0, 2, 4 ] ] )

# 문제 4: 1차원 배열 슬라이싱
print( x[1:4] )
print( x[:3] )
print( x[ : : 2 ])

# 문제 5: 2차원 배열 슬라이싱
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
print( x[ : 2 , 1 : ])

# 문제 6: 축 기준 슬라이싱
print( x[0, : ] )
print( x[ : ,0] )

# 문제 7: 슬라이싱의 참조 특성
x = np.array([1,2,3,4,5])
y = x[1:4]
y[0] = 99
print( x )
# 값이 변함! -> 슬라이싱은 원본을 담고 있기 때문에... 복사본으로 주는 게 아님!

# 문제 8: 요소별 사칙연산
x = np.array([1,2,3])
y = np.array([4,5,6])
print( x + y )
print( x - y )
print( x * y )
print( x / y )

# 문제 9: 브로드캐스팅 및 수학 함수
x = np.array([1,2,3])
print( x + 2 )
print( x * 3 )
x = np.array([1,4,9])
print( np.sqrt( x ) )

# 문제 10: 논리 및 비교 연산
x = np.array([True, False, True])
y = np.array([False, False, True])
print( np.logical_and( x, y ) )
print( np.logical_or( x, y ) )
x = np.array([1,2,3])
y = np.array([1,2,4])
print( np.array_equal( x, y ) )

