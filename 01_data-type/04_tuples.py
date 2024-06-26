

# Sequence Type 
# 값이 연속적으로 나열된 자료형을 의미하며 다음 자료형이 해당된다
# str :  문자열 값을 가지는 자료형
# list : 여러값을 담을 수있는 가변형 자료형
# tuple : 여러 값을 담을 수있는 불변형 자료형

name = 'ohgiraffers'
print(type(name))

list = [0,1,2,3]
print(type(list))

# tuple : 불변형 자료형 (바꿀수 없다.)
tuple = (1,2,3)
print(type(tuple))





### Tuple ###

# python 에서 사용하는 자료형 중 하나로, 여러개의 값을 하나의 데이터 구조로 묶어서 관리할 수있는 불변 시퀀스
# List와 유사하지만 한번 생성되면 각 요소 값을 수정하거나 삭제 할 수 없다.
# 주로 데이터의 집합을 안전하게 유지하거나, 함수에서 여러 값을 반환 할 때 사용.

safari_tupe = ("Bear", "Koara", "Gorilla", "Pig")

print(safari_tupe)



# tuple은 중첩으로 표현 가능
tuples = (1 ,2, 'hello'),('test', 1, 2, 3, 4)
print(tuples)
print(tuples[0])
# 0번째 인덱스 안의 2번째 인덱스 출력
print(tuples[0][2])




# Tuple 연산 
# 불변 객체이므로 요소 값을 한번 할당하면 추가, 수정, 삭제가 불가하다.
# tuples[0] = (1,2,3,4)
testList = (1,2,3,4)
print(id(testList))
        # id: 주소값

testList = (3,4,5)
print(id(testList))
# 아예 새로운 주소값이 생김.



# 튜플간 연산

another_safari_tuple = ("monkey", "tiger", 'wolf')
print(safari_tupe + another_safari_tuple)
print(len(safari_tupe + another_safari_tuple))
