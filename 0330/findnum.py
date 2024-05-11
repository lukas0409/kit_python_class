# num이라는 이름의 빈 리스트 생성
num = []

num_cnt = 10
tmp = 0

# 정수 10개 입력받아 num에 append
for i in range (0,num_cnt):
    plus = int(input("Input number: "))
    num.append(plus)

tmp = num[0]

# 가장 작은 수 찾기
for a in range (0,num_cnt):
    if num[a] < tmp:
        tmp = num[a]

# print
print("가장 작은 수 : %d" % tmp)