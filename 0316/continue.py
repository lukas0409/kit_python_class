count = 0

while True:
    num = int(input("Input number: "))
    if num <= 10:
        continue 
    if num % 2 == 1:
        break
    count = count + 1

print("Total count = %d" % count)