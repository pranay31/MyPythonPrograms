# Write a program to remove duplicates from array in Java

l = [2, 10, 4, 2, 5, 3, 6, 7, 3, 5, 8, 9, 10, 4]
uniq = set(l)
res = []
for i in l:
    if i in uniq:
        if i not in res:
            res.append(i)
print res
