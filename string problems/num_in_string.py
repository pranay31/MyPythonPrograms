# How to check if a String contains only digits
try:
    a = "1234a"
    num = int(a)
    print "it has only numbers"
except:
    print "it does not have the numbers"

# or we can use a.isdigit() function to check
