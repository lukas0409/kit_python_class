#리스트 생성
num = []

x = 1
cen = 0
cnt = 0
temp = 0

# 리스트 값 입력
while x > 0:
    x = int(input("Input number: "))
    if x == -1:
        break
    num.append(x)
    cnt = cnt + 1

cen = int(cnt / 2)

# 리스트 값 반전
for i in range (0, cen):
    temp = num[i]
    num[i] = num[cnt-1-i]
    num[cnt-1-i] = temp

print(num)