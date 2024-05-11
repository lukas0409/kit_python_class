# 문자열 오름차순 정렬

num = []
cnt = 0

while True:
    n = input("데이터 입력: ")
    if n == "-1":
        break
    num.append(n)
    cnt = cnt + 1


for i in range(0, cnt):
    tmp = num[i]
    idx = i
    for j in range(i, cnt):
        if num[j] < tmp:
            tmp = num[j]
            idx = j

    temp = num[i]
    num[i] = num[idx]
    num[idx] = temp

print(num)