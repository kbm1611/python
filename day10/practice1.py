# 넘파이: 파이썬 언어 기반으로 수치 계산 특화된 라이브러리( AI )
# 파이썬에 *리스트*가 존재하는데 굳이 *넘파이배열*을 사용하는 이유? 수치 관련 기능 차이

#문제1: ndarray 생성
import numpy as np
array1 = np.array( [ 10, 20, 30, 40 ] )
array2 = np.array( [ [ 1, 2 ], [ 3,4 ] ] )
print( array1 )
print( array2 )

# 문제2: 특정 값으로 채워진 배열
print( np.zeros( ( 3, 4 ) ) )
print( np.ones( ( 2, 5 ) ) )
print( np.full ( ( 3, 3 ), 9 ) )

# 문제3: 연속된 수와 균등 간격 배열
# 1. np.arange를 사용하여 10부터 50까지 5씩 증가하는 배열을 생성하시오.
print( np.arange( 10, 50+1, 5 ) ) 
# 2. np.linspace를 사용하여 0부터 10 사이를 균등하게 5개의 구간으로 나눈 배열을 생성하시오.
print( np.linspace( 0, 10, 5 ) )

# 문제4: shape와 size 확인
# x = np.array( [ 1, 2, 3 ], [ 4, 5, 6 ] ) 배열의 모양과 전체 요소의 개수를 출력하는 코드를 작성하시오.
x = np.array( [ [ 1, 2, 3 ], [ 4, 5, 6 ] ] )
print( x.shape )
print( x.size )

# # 문제 5: 차원 확인 (ndim)
# 1차원 배열 [1, 2, 3]과 3차원 배열 [[[1], [2]], [[3], [4]]]를 각각 생성한 후, 
# .ndim 속성을 사용하여 각각 몇 차원인지 출력하시오.
x = np.array( [ 1, 2, 3 ] )
print( x.ndim )
y = np.array( [ [ [ 1 ], [ 2 ] ], [ [ 3 ], [ 4 ] ] ] )
print( y.ndim )

# # 문제 6: 데이터 타입(dtype) 확인
# 실수형 데이터 [1.5, 2.5, 3.5]를 가진 배열을 만들고,
# 이 배열의 요소들이 어떤 데이터 타입으로 저장되어 있는지 출력하시오.
x = np.array( [ 1.5, 2.5, 3.5 ] )
print( x.dtype )

# # 문제 7: 배열 평탄화 순회 (flat)
# 2행 2열의 2차원 배열을 생성한 후, .flat 속성과 반복문(for)을 사용하여
# 모든 요소를 한 줄씩 차례대로 출력하시오.
x = np.array( [ [ 1, 2 ], [ 3, 4 ] ] )
for i in x.flat:
    print( i )

# # 문제 8: 타입 지정 생성
# 배열을 생성할 때 dtype 옵션을 사용하여 다음 조건에 맞는 배열을 만드시오.
# 정수형(int32) 타입의 배열 [1, 2, 3]
# 불리언(bool) 타입의 배열 [True, False, True]
x = np.array( [ 1, 2, 3 ], dtype = np.int32  )
x = np.array( [ True, False, True ], dtype = np.bool_ )

# # 문제 9: 형변환 (astype)
# 실수형 배열 x = np.array([1.1, 2.9, 3.5])를 생성한 후,
# .astype() 메서드를 사용하여 소수점이 제거된 정수형(int32) 배열로 변환하고 출력하시오.
x = np.array( [ 1.1, 2.9, 3.5 ] )
y = x.astype( np.int32 )

# # 문제 10: 바이트 문자열 배열
# 과일 이름 리스트 ['apple', 'banana']를 넘파이 배열로 만들되,
# 데이터 타입을 np.bytes_로 지정하여 생성하고 결과를 확인하시오.
x = np.array( [ 'apple', 'banana' ], dtype = np.bytes_ )
print( x.dtype ) # |S6
