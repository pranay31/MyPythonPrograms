def fib(num):
    first=0
    second=1
    yield first
    yield second
    count = 2
    while count < num:
        next=first+second
        yield next
        first=second
        second=next
        count += 1
f = fib(11)

print (f)
