def dec(func):
    param = "pranay"
    def inner(lname):
        return "My full name :" + param + lname
    return inner

@dec
def last(lname):
    return lname


print last("nevuri")
