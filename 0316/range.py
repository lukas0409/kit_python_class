# 1부터 10까지 짝수의 합
# range(num1, num2): num1부터 num2-1까지의 숫자 생성

acc = 0

for num in range (1,11):
    if num % 2 == 0:
        acc = acc + num

print("Sum of 1 to 10 is %d" % acc)