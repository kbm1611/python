# [1] min, max, sum
numbers = [ 103, 52, 273, 32, 77 ]
print( min(numbers) )   # 최소값
print( max(numbers) )   # 최대값
print( sum(numbers) )   # 누적합계

# [2] reversed( 리스트 ), 이터레이터 반환
print( reversed(numbers) ) # <list_reverseiterator object at 0x000001D60A06F340>

for i in reversed( numbers ) :
    print( i ) # 역순으로 출력

# [3] enumerate( 리스트 ), 인덱스와 자료 순회 가능하다.
print( enumerate( numbers ) ) # <enumerate object at 0x00000227CC11AB60>
print( list( enumerate( numbers ) ) ) # [(0, 103), (1, 52), (2, 273), (3, 32), (4, 77)]

for index, value in enumerate( numbers ):
    print( index, value )

# [4] items( )
example_dictionary = { '키A' : '값A' , '키B' : '값B' , '키C' : '값C'}
print( example_dictionary.items() ) # dict_items([('키A', '값A'), ('키B', '값B'), ('키C', '값C')])

# [5] 리스트내 반복문 사용 , 0부터 20사이의 짝수 갖는 리스트
# (1)
array = [ ]
for i in range( 0, 20, 2 ):
    array.append( i )
print( array ) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# (2) [ 계산식 for 반복변수 in 반복할 수 있는 것 if 조건식 ]
array = [ i for i in range( 0, 20, 2) ]
print( array ) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

array = [ i+1 for i in range(0, 20, 2) if i != 10 ]
print( array )

# [6] 문자열 여러줄 입력하기
# (1) """
print( """안녕하세요1
안녕하세요2""")

# (2) \n
print( "안녕하세요1\n안녕하세요2")

# (3) ( ) 소괄호 안에서 여러개 문자 연결
print( ( "안녕하세요1\n" "안녕하세요2" ) )

# (4) 조합문자열.join(문자열리스트), 리스트내 요소 사이에 조합문자열 연결
print( "\n".join( ["안녕하세요1", "안녕하세요2"] ) )