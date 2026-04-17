
# 딕셔너리란? 키를 기반으로 값을 저장하는 것
# vs JS(JSON) vs JAVA(map/dto)

# [1] 선언 , {"키" : 값, "키" : 값}
dict_a = { "name" : "어벤져스 엔드게임", "type" : "히어로 무비" }

# [2] 호출
print(dict_a)
#print( dict_a.name ) # JS 가능하지만 오류 발생
print( dict_a["name"] )
print( dict_a.get( "name" ) ) # JAVA MAP 처럼 호출 가능
# print( dict_a["origin"] ) # 없는 키이면 오류 발생

# [3] 딕셔너리 값 추가 하기 , 딕셔너리명[ 'key' ] = value
dict_a[ "price" ] = 1000
print( dict_a )

dict_a[ "price" ] = 2000 # 만약에 존재하는 key이면 value 수정 # key는 중복 없음
print( dict_a )

# [4] 딕셔너리 키/값 제거하기, del 딕셔너리명[ 'key' ]
del dict_a[ 'price' ]
print( dict_a )

# 반복문과 딕셔너리 관계
# for key in dictionary :
#   코드

for key in dict_a:
    print(key , ':' , dict_a[key] )


# p.227 확인문제

# 확인문제2
pets = [
    {"name" : "구름", "age" : 5},
    {"name" : "초코", "age" : 7},
    {"name" : "하양", "age" : 3}
]

for pet in pets:
    print(f'{pet["name"]} {pet["age"]}살')


# 확인문제3
numbers = [1,2,6,5,3,2,6,8,5,6,6,8,2,3,1,2,8,9,0]

counter = {}

for number in numbers:
    if number not in counter:
        counter[number] = 0
    counter[number] = counter[number] + 1

print(counter)

# 확인문제4
character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : [ "베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    value = character[key]

    if type(value) is str:
        print(f'{key} : {value}')
    elif type(value) is dict:
        for inkey in value:
            print(f'{inkey} : {value[inkey]}')
    elif type(value) is list:
        for item in value:
            print(f'{key} : {item}')
    else:
        print('value값이 str, dict, list가 아닙니다.')