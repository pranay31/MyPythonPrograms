#How to check if two Strings are anagrams of each other

def anagram(first, second):
    if len(first) != len(second):
        return False

    f,s = first.lower(), second.lower()
    if f == s:
        return False

    return sorted(f) == sorted(s)


result = anagram("army", "mary")
print result


