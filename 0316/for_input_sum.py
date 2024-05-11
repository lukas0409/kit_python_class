# 사용자에게 숫자값 10개 받아 합과 평균 계산

acc = 0

for num in range (0,10):
    num = int(input("Input number: "))
    acc = acc + num

ave = acc / 10

print("Sum is %d and average %d" % (acc, ave))
print("average is %d" % ave)