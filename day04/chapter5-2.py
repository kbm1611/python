
# 재귀함수란? 현재 실행 중인 함수(자신)를 다시 호출 하는 것

# [1] 반복문으로 팩토리얼 구하기.
def factorial(n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    
    return output

print("반복문 5! = ", factorial(5) )

# [2] 재귀함수로 팩토리얼 구하기.
# factorial2( 5 ) -> 5 * 재귀 (안끝남)                                  5 * 4 * 3 * 2 * 1 * 1
# factorial2( 4 ) ->    4 * 재귀 (안끝남)                           4 * 3 * 2 * 1 * 1
# factorial2( 3 ) ->        3 * 재귀 (안끝남)                   3 * 2 * 1 * 1
# factorial2( 2 ) ->            2 * 재귀 (안끝남)           2 * 1 * 1
# factorial2( 1 ) ->                1 * 재귀 (안끝남)   1 * 1
# factorial2( 0 ) ->                    return 1 (끝남) factorial2 함수는 총 몇번 호출? 6번 호출, return 6번 되어야 한다.

def factorial2(n):
    if( n == 0 ): return 1
    else: return n * factorial2( n - 1 ) # 재귀함수 호출

print("재귀 5! = ", factorial2(5) )

# [3] 피보나치 수열 1 , 1번째 수열 : 1, 2번째 수열 : 2, n번째 수열: n-1수열 + n-2수열

# 문제점 : 재귀수가 많아서 계산식이 오래 걸린다.

def fibonacci( n ):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci( n - 1 ) + fibonacci( n - 2 )

print( fibonacci( 20 ) )

dictionary = {
    1: 1,
    2: 1
}

# [4] 메모화 : 객체를 만들어 기존에 연산한 걸 또 연산하지 않게 시키는 작업 -> 작업 효율 극대화

counter = 0     # 함수 밖에 있는 변수
def fibonacci_memo( n ):
    global counter # 함수 박에 있는 변수 호출
    counter += 1
    print( '---->' ,counter )

    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci_memo( n - 1 ) + fibonacci_memo( n - 2 )
        dictionary[n] = output
        return output

print( fibonacci_memo(10) )

allCnt = 9
canMinCnt = 2
canMaxCnt = 10
memo = {}

def problem(leftCnt, minCnt):
    key = str([leftCnt, minCnt])
    if key in memo:
        return memo[key]
    if leftCnt < 0:
        return 0
    if leftCnt == 0:
        return 1
    
    # 재귀 처리 
    output = 0
    for i in range( minCnt, canMaxCnt + 1):
        output += problem(leftCnt - i, i)

    # 메모화 처리
    memo[key] = output
    # 종료
    return output

print( problem( allCnt, canMinCnt) )

