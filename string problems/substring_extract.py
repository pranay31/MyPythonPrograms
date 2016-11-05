l = 'IBM Cognitive resolve cognition | IBM \"Cognitive\" resolve cognition | IBM Cognitive resolve cognition | \
IBM Cognitive resolve cognition|'
flag = '|'
if flag in l:  # $ is the flag
    dex1 = l.index(flag)
    print "dex1 :", dex1
    subline = l[dex1 + 1:-1]  # leave out flag (+1) to end of line
    print "subline :", subline
    dex2 = subline.index(flag)
    print "dex2", dex2
    string = subline[0:dex2].strip()  # does not include last flag, strip whitespace
    print string
print l
