# 연습문제
a = 7
b = 3
result = a + b
print(result)

# 해당 부분 변경
sugyeong = "abcd"
sugyeong = sugyeong.replace("a", "A")
print(sugyeong)

# 거꾸로 뒤집기
# 1. 주어진 변수 및 데이터를 할당
hyundai = "Python"
print(len(hyundai))
# 2. 슬라이싱 해보기
safety = hyundai[5] + hyundai[4] + hyundai[3] + hyundai[2] + hyundai[1] + hyundai[0]
print(safety)

# 리스트의 평균 구하기
nums = [1, 2, 3, 4, 5]
# nums = list(range(1,6))도 가능
avg = (nums[0] + nums[1] + nums[2] + nums[3] + nums[4])/len(nums)
print(avg)

# 주어진 딕셔너리에서 해당 값을 추출하는 파이썬 코드
dic = {'apple': 3, 'banana': 5, 'cherry': 2}
print(dic['banana'])
