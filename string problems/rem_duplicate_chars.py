# How to remove duplicate characters from String
foo='bananas'
result = "".join([j for i,j in enumerate(foo) if j not in foo[:i]])
print result

print 50 * "-"

foo = 'alabama'
res = ''.join(sorted(set(foo), key=foo.index))
print res

