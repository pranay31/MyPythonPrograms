# There is an array with every element repeated twice or more, except one or more. Find these element

l = [1, 2, 2, 3, 1, 4, 4, 5, 5, 6, 5,2,3,10,1 ]
res = []
for i in range(0, len(l)):
    fst = l[i]
    for j in range(i+1, len(l)):
        sec = l[j]
        if fst == sec:
            res.append(fst)

for i in l:
    if i not in res:
        print i
