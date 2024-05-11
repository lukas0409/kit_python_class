#리스트 생성
num = []
num1 = []

x = 1
i = -1

# 리스트 값 입력
while x > 0:
    x = int(input("Input number: "))
    if x == -1:
        break
    num.append(x)
    i = i + 1

# 리스트 값 반전
for a in range (0, i + 1):
    num1.append(num[i-a])

print(num1)