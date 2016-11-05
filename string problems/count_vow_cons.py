# How to count number of vowels and consonants in a String

st = "How to count number of vowels and consonants in a String"
d = {}
l = list("aeiou")
c = list("bcdfghjklmnpqrstvwxyz")
for char in st:
    if char in d:
        d[char] += 1
    else:
        d[char] = 1

count_vow = 0
count_cons = 0
for n in d:
    if n in l:
        count_vow += 1
    elif n in c:
        count_cons += 1

print count_vow, count_cons






