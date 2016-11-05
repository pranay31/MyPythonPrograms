l = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
count = 1
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[j] == l[i]+1 or l[j] == l[i]-1:

            count += 1

print count
