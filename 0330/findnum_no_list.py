num = []

num_cnt = 10
tmp = 0

for num in range (0,10):
    num = int(input("Input number: "))
    if num >= tmp:
        tmp = num

print(tmp)