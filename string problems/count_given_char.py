# How to count occurrence of a given character in String
def count(ipt, letter):
    d = {}
    for i in ipt:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for j in d:
        if letter == j:
            return d[j]
    return "this letter is not in the string"

a = raw_input("enter the letter :")
inp = "How to count occurrence of a given character in String"
b = count(inp, a)
print b
