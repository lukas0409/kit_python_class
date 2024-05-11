# 빈 리스트 생성
num = []
num1 = []

num_cnt = 10

# 정수 10개 입력받아 num에 append
for i in range (0,num_cnt):
    plus = int(input("리스트 데이터: "))
    num.append(plus)

# 이동 횟수 입력
shi = int(input("이동 횟수: "))

# 이동 방향 입력
way = int(input("이동 방향 (오른쪽:0 왼쪽:1):"))

# 오른쪽 이동 시 shi 변수 반전
if way == 0:
    shi = num_cnt - shi

# R부분 num1에 append
for a in range (shi,num_cnt):
    num1.append(num[a])

# L부분 num1에 append
for a in range (0,shi):
    num1.append(num[a])



print(num1)