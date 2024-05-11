# 사용자가 입력한 n개의 정수의 합과 평균 계산
# -1을 입력받으면 멈춤

acc = 0
count = 0
num = 1

while num > 0:
    num = int(input("Input number: "))
    if num == -1:
        break
    acc = acc + num
    count = count + 1

ave = acc / count

print("Sum is %d and average %d" % (acc, ave))