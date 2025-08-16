def is_anagram(s1, s2):
    if sorted(s1) == sorted(s2):
        result = True
    else:
        result = False
    return result

print(is_anagram("listen", "silent"))
print(is_anagram("python", "typhon"))
print(is_anagram("hello", "world"))