#How to program to print first non repeated character from String
check_string = "Morning"
count = {}
l = []
for s in check_string:
  if s in count:
      count[s] += 1
  else:
      count[s] = 1
      l.append(s)

print l[0]


