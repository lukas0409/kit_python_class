num = []

cnt = 0
while True:
    n = int(input("데이터 입력: "))
    if n == -1:
        break
    num.append(n)
    cnt = cnt + 1

tmp = num[0]
# 가장 작은 수 찾기
for a in range (1, cnt):
    if num[a] < tmp:
        tmp = num[a]
        idx = a
# print
print("가장 작은 수의 인덱스 : %d" % idx)