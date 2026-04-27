
# isinstance( 객체, 클래스명 ), 만약에 해당 객체가 클래스로 만들어졌다면 True, False
# vs JAVA : 객체 instanceof 클래스명

# [1] 클래스 선언
class Student:
    count = 0
    def study( self ):
        print("공부를 합니다.")
    def __str__( self ):    # str() 함수 호출될 때 자동으로 실행되는 함수
        return "학생"
    def __eq__(self, value):    # == 호출될 때 자동으로 실행되는 함수
        return 80 == value
    
    def func1( self ):
        return Student.count+1 # 클래스 변수 호출
    
    # cls(클래스) vs self(인스턴스)
    # 클래스 함수 vs JAVA : static
    @classmethod    # 데코레이터
    def print( cls ): # cls( class ) 해당 클래스 가리킴.
        print("클래스 함수 호출")
        print( cls.count )
    
class Teacher:
    def teach( self ):
        print("학생을 가르칩니다.")

# [2] 인스턴스 생성
classroom = [ Student(), Student(), Teacher(), Student(), Student() ]
# [3] 리스트내 인스턴스들의 타입 확인
for person in classroom:
    if isinstance( person, Student ):
        person.study()
    elif isinstance( person, Teacher ):
        person.teach()
# [4]
print( str( classroom[0] ) )
print( classroom[0] == 90 )
print( classroom[0] == 80 )

# [5] 클래스 변수 호출, 클래스명.변수명
print( Student.count )  # 클래스변수는 인스턴스 없이 호출 가능
print( classroom[0].func1() ) # 1

# [6] 클래스 함수 호출, 클래스명.함수명()
Student.print()

#[7] 프라이빗 변수 ㅡ , __변수명 vs JAVA : private
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius # 프라이빗 변수에 매개변수 대입
    def get_cirumference( self ):
        return math.pi * self.__radius # 클래스 내부에서
    def get_area( self ):
        return math.pi * (self.__radius ** 2)
    # [8] 게터와 세터, 프라이빗 변수를 외부에서 간접 접근 허용 함수
    @property
    def radius( self ):
        return self.__radius
    @radius.setter
    def radius( self, value ):
        self.__radius = value

Circle( 20 )    # 인스턴스 생성 후 변수에 저장하지 않았으므로 GC가 자동으로 인스턴스 삭제
circle = Circle( 10 )
# print( circle.radius ) # 프라이비 변수이므로 직접 호출 시 오류 발생

print( circle.radius ) # 간접 접근, getter 10
circle.radius = 20 # 간접 전근, setter
print( circle.radius ) # 간접 접근, getter 20

# [9] 상속
class Parent:
    def __init__(self):
        self.value = "테스트"
        print( "부모 클래스의 생성자가 호출 되었습니다." )
    def test( self ):
        print( "부모 클래스의 test() 메소드 입니다." )

class Child( Parent ): # class 클래스명( 상위 클래스명 ):
    def __init__( self ):
        super().__init__( ) # 부모의 생성자를 호출한다.
        print( "자식 클래스의 생성자 호출되었습니다." )

child = Child() # 상속된 인스턴스가 생성될 때 : 자식이 생성되면 부모도 같이 생성된다.
child.test()
print( child.value ) # 자식은 부모의 멤버변수와 멤버함수 사용할 수 있다. <물려받음>

# [10] 상속 이용한 나마느이 예외클래스 만들기
class CustomException( Exception ): # Exception 클래스로부터 상속 받는다.
    def __init__(self, message, value):
        super().__init__( )
        self.message = message
        self.value = value
    # 오버라이드/재정의 : 부모에 정의도어 있는 함수를 자식이 다시 정의
    def __str__(self):
        return self.message
    def print( self ):
        print( "#### 오류 정보 ###" )
        print( "메시지: ", self.message )
        print( "값: ", self.value )
        
# 강제로 예외 발생시키기
try:
    raise CustomException( "강제예외", 10)
except CustomException as e:
    print( e )