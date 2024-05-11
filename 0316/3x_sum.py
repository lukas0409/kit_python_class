# 사용자가 입력한 n까지 정수 중 3의 배수의 합 계산

acc = 0
a = 1

num = int(input("Input number: "))

while num >= a:
    if a % 3 == 0:
        acc = acc + a
    a = a + 1

print("Sum is %d" % acc)