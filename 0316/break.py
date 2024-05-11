count = 0

while True:
    num = int(input("Input number? ")) # num 입력
    if num % 2 == 1: # 2로 나눌 때 나머지가 1이면 (홀수이면)
        break # while문 종료
    count = count + 1

print("Total count = %d" % count)