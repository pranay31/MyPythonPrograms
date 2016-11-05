l = [1,2,3,4,5,6]
res = []
for i in range(len(l)):
    m = l[i]
    rem = l[:i] + l[i+1:]
    print "l[i]",l[:i]
    print "l[i+1:]", l[i+1:]
    print "rem :", rem
