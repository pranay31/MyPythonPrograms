# How to find the missing number in integer array of 1 to 100

def miss_num(*args):
    i = args[0]
    while i < len(args):
        if args[i] + 1 == args[i + 1]:
            if args[-1] == args[i+1]:
                break
            else:
                i +=1
        else:
            return "missing element: ", args[i] + 1
    return "no missing element"

print miss_num(3,4,5,6,7,8,10,11,12,13)


