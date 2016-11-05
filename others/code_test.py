import sys
import math
def check_formatting(lowerBound, upperBound, num_primes):
    try:
        assert lowerBound < upperBound
        assert type(lowerBound) is int
        assert type(upperBound) is int
        assert type(num_primes) is int
        assert num_primes > 0
    except AssertionError as validation_error:
        print ("input validation failed {0}".format(validation_error))
        sys.exit(-1)


def isPrime(num_to_be_checked):
    square_root_of_number = int(math.ceil(math.sqrt(num_to_be_checked)))
    Is_prime = True
    for current_number in range(2, square_root_of_number + 1):
        if num_to_be_checked % current_number == 0:
            Is_prime = False
    return Is_prime


if __name__ == '__main__':
    lowerBound = 3
    upperBound = 50
    num_primes = 10
    primes = []
    notPrimes = [0, 1]
    check_formatting(lowerBound, upperBound, num_primes)
    for i in range(lowerBound, upperBound):
        if isPrime(i):
            primes.append(i)
            print "inside if", primes
    if len(primes) >= num_primes:
        print "second if", primes[:num_primes]
    else:
        print primes





