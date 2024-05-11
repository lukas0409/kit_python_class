b = 0
a = int(input("input data: "))

for i in range (0, a):
    for j in range (i, a):
        b = i * j
        print("%d X %d = %d" % (i, j, b))