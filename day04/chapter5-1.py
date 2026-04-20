# 함수 만들기
def functionName():     # 함수의 정의/만들기
    print("안녕하세요1")
    print("안녕하세요1")
    print("안녕하세요1")

functionName()          # 함수 호출/사용

# 매개변수 : 함수 호출/사용할 때 인자값 저장하는 변수
def func2( value, n):       # 매개변수 2개 선언
    for i in range( n ):    # 매개변수 사용
        print( value )

func2( "안녕하세요2", 5 )     # 함수에게 인자값 2개 전달

# 가변 매개변수: 매개변수의 개수가 변할 수 있다.
def func3( n, *values ):
    for i in range( n ):
        for value in values:
            print( value )
        print( )

func3( 3, "안녕하세요3", "즐거운", "파이썬 프로그래밍")

# 기본 매개변수: 만약에 함수 사용/호출할 때 인자값이 없으면 기본 값 대입
def func4( value , n = 2 ):        # 매개변수에 변수명=기본값으로 인자값이 없을 때 대입된다.
    for i in range( n ):
        print( value )

func4( "안녕하세요4" )

# 키워드 매개변수 : 매개변수 이름ㅇㄹ 직접 지정하여 매개변수에 대입하는 방법
def func5( *values, n = 2):
    for i in range( n ):
        for value in values:
            print( value )
        print()

func5("안녕하세요5", "즐거운", "파이썬 프로그래밍", 3) # n 매개변수에 3 대입 안된다.
func5("안녕하세요5", "즐거운", "파이썬 프로그래밍", n = 3) # 직접 매개변수명 작성하여 대입하면 된다.

# 리턴? 함수 종료시 반환되는 키워드
# 반환값이 없는 리턴
def func6():
    return
print( func6() )        # None, 반환값이 없다.

# 반환값이 있는 리턴
def func7():
    return 100

print( func7() )        # 100