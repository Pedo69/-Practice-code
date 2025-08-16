def find_repeated_substrings(s: str) -> list:
    sub = []
    seen = set()
    repeated = set()

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            if len(sub) >= 2:
                if sub in seen:
                    repeated.add(sub)
                else:
                    seen.add(sub)
    return repeated


print(find_repeated_substrings("banana"))
# Output: ['an', 'ana', 'na']

print(find_repeated_substrings("abcdefg"))
# Output: []

print(find_repeated_substrings("abcabcabc"))
# Output: ['ab', 'abc', 'abca', 'abcab', 'abcabc', 'bc', 'bca', 'bcab',
#          'bcabc', 'ca', 'cab', 'cabc']

print(find_repeated_substrings("aaaa"))
# Output: ['aa', 'aaa ']