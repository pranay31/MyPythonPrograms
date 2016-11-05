a = range(1,25)
print a
p = "out"
q = "think"
result = []
for i in a:
    if i == 3 or i == 4 or (i%3 == 0 and i%4 == 0):
        result.append(p+q)
    elif i%3 == 0:
        result.append(p)
    elif i%4 == 0:
        result.append(q)
    else:
        result.append(i)

print result
