hello_world = "엄마가 말했다. '밥 먹었니?'"
print(hello_world)

name = "홍길동"
money = 100
print("안녕하세요. "+ name + "님 반갑습니다.")
print("입력하신 금액은 ", money, "원 입니다.")

# 데이터 출력 시, % 기호 사용하는 방법
name = "강수경"
print("안녕하세요. 저의 이름은 %s입니다." %name)

money = 10000
print("입력하신 금액은 %d원 입니다." %money)

# 문자열 길이 구하기
hello_world = "엄마가 말했다. '밥 먹었니?'"
print(len(hello_world))

# 문자열 슬라이싱
자유로운_문자열 = "아무 문자열이나 한 번 입력해보세요."
print(len(자유로운_문자열))
print(자유로운_문자열[0:2])

# 문자열 치환
date = "2024.07.04"
print("바꾸기 전의 데이터 : ", date)
date = date.replace(".", "-")
print("바꾼 후의 데이터 : ", date)

# 문자열 여러 줄 출력하기
자유로운_문자열 = "아무 문자열이나 한 번 입력해보세요.\n현대 취뽀 가자."
print(자유로운_문자열)

# 리스트에 요소 추가/삭제하기
num_list = [1,2,3,4,5]
num_list.append(6)
print(num_list)
num_list.remove(3)
print(num_list)
