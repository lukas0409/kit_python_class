num = []
acc = 0

for a in range (0, 10):
    b = int(input("Input number: "))
    num.append(b)

for a in range (0, 10):
    acc = acc + num[a]

ave = acc / 10

print("Average of these numbers : %s" % ave)