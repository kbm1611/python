import pandas as pd

# 문제1
sales = { 'mon' : 100, 'tue' : 200, 'wed' : 300 }
sales_Series = pd.Series( sales )
sales_Series = sales_Series.rename( { 'mon' : '월', 'tue' : '화', 'wed' : '수' } )
print( sales_Series )

# 문제2
data = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
data[1:4] = data.iloc[1:4] * 2
data.loc['d'] = 100
print( data )

# 문제3
s1 = pd.Series([1,2], index=['a','b'])
s2 = pd.Series([3,4], index=['a','c'])

s3 = pd.concat( [s1, s2] )
print( s3.loc['a'] )

# 문제4
data = pd.Series([15,25,35,45,55])
data[ ( data > 30 ) & ( data < 50 ) ] = data[ ( data > 30 ) & ( data < 50 ) ] + 5
print( data )

# 문제5
grade = pd.Series(['A','B','A','C','B','A','A','B'])
print( grade.value_counts() )
print( grade.value_counts( normalize=True ))

# 문제6
s1 = pd.Series([10,20], index=['a','b'])
s2 = pd.Series([30,40], index=['b','c'])
print( s1 + s2 )
# 결측치가 발생한 위치: 인덱스 a와 c, 인덱스 기준으로 + 연산을 실행하기 때문에

# 문제7
# 1차 정렬 이후에 유지하기 위해서, 1차 정렬에 kinde 속성에'stable' 적용하여 유지할 수 있다.
# sort( 2차 정렬 ).sort( 1차 정렬 )
data = pd.Series([20,10,20,30], index=['d','c','a','b'])
result = data.sort_index().sort_values( ascending = False, kind='stable' )
print( result )

# 문제8
data = pd.Series([10,20,30,40], index=['A','B','A','B'])
data = data.groupby(level = 0).agg(['sum','mean'])
print( data )

# 문제9
score = pd.Series([80,90,70], index=['math', 'eng', 'sci'])
weight = pd.Series([0.4, 0.3, 0.3], index=['math', 'eng', 'sci'])
total = score * weight
print( total )

# 문제10
data = pd.Series([10,30,20,40], index=['a','b','c','d'])
x = data[ data > 25 ]
y = x.reset_index( drop = True )
print( y )
