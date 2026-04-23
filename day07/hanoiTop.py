
# n은 원판 갯수, source는 시작 기둥, target는 목적 기둥, other은 보조 기둥
count = 0
def hanoi(n, source, target, other):
    global count
    if n == 1:
        # print(f"{source}탑 -> {target}탑")
        count += 1
        return
    
    # n-1개를 보조 기둥으로 이동
    hanoi( n - 1, source, other, target )

    # 마지막 원판 옮기기 n번째 원판
    # print(f"{source}탑 -> {target}탑")
    count += 1

    # 보조 기둥에 있는 n-1개를 목적지 기둥으로 이동
    hanoi(n - 1, other, target, source)

n = int( input("원판의 개수를 입력해주세요: ") )
hanoi(n, "A", "B", "C")
print("이동 횟수는 {}회입니다.".format(count))

#재귀 함수를 잘하는 방법
# 종료조건 생각하기(언제 끝날 지)
# 작업을 어떻게 쪼갤 것인지 생각하기