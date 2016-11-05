# How to find the smallest positive integer value that cannot be represented as sum of any subset of a given array

l = [2,3,6,7]
res = 1
for i in range(0,len(l)):
    if l[i] <= res:
        res += l[i]
    else:
        break

print res
