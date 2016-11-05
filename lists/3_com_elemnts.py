input1 = [1, 5, 10, 20, 40, 80]
input2 = [6, 7, 20, 80, 100]
input3 = [3, 4, 15, 20, 30, 70, 80, 120]
res = []

for i in input1:
    if i in input2:
        if i in input3:
            res.append(i)

print res


