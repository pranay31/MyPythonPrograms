# How to find all Pairs in Array of Integers whose Sum is equal to a given Number

l = [1,2,3,4,5,6,7,8,9,10]
sum = input("enter the sum :")
for i in range(0, len(l)):
    fst = l[i]
    for j in range(i+1, len(l)):
        sec = l[j]
        if fst + sec == sum:
            print fst,sec
        elif fst + fst == sum:
            print fst,fst
            break










