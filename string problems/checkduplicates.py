# How to Print duplicate characters from String?
check_string = "java"
count = {}
for s in check_string:
    if s in count:
        count[s] += 1
    else:
        count[s] = 1

for key in count:
    if count[key] > 1:
        print key

print 30 * "-"

st = "How to Print duplicate characters from String"
mydict = {}
for char in st:
    mydict[char] = mydict.get(char, 0)+1
for key in mydict:
    if mydict[key] > 1:
        print key

print 30 * "-"





