

# 변수명 작성 규칙

# 1. 변수명은 스네이크 케이스로 작성하며, 대소문자를 구분

team_name = '오지라퍼스'
Team_name = 'ohgiraffers'

print(team_name)
print(Team_name)



# 2. 영문과 숫자를 혼합해 작성할 수 있다. (단, 숫자를 가장앞에 작성 불가)
team_1_name = '오지라퍼스'



# 3. 한글 변수명도 지정 가능
팀명 ='오지라퍼스'



# 4. 언더바(_)를 제외한 특수문자는 사용 불가
# team_@_name = '불가능'



# 5. 예약어를 사용할 수 없다.
# else = '불가능'


###  언더바(_) ###
# 값을 무시하고 싶은 경우, 특정 값을 무시하기 위한 용도로 사용할 수 있다.
x, *_, y = (1,2,3,4,5)
print(x)
print(y)

# 언더바가 붙어있는 메소드는 프라이빗으로 사용하자는 개발자들끼리의 약속이 되어있음.



# 숫자값의 자릿수 구분을 위한 구분자로 사용 가능
# 구분을 하기위한 목적
million = 1_000_000
print(million)