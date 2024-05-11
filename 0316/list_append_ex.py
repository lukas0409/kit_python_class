# 리스트 num1, num2, num3 생성
# num3은 빈 리수투
num1 = [10, 20, 30, 40, 50]
num2 = [60, 70, 80]
num3 = []
# 리스트 num1에 있는 데이터를 읽어서 리스트 num3에 저장
for i in range(0, 5):
    num3.append(num1[i])
# 리스트 num2에 있는 데이터를 읽어서 리스트 num3에 저장
for i in range(0, 3):
    num3.append(num2[i])
# 리스트 num3에 있는 데이터 출력
    print(num3)