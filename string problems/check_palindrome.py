# How to check if String is Palindrome
def palindrome(st):
    if st == st[::-1]:
        return True
    return False

result = palindrome("this")
print result
