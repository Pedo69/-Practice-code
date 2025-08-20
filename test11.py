def find_repeated_substrings(s: str) -> list:
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
    
    # return as sorted list for consistent results
    return sorted(repeated, key=lambda x: (len(x), x))


print(find_repeated_substrings("banana"))
# ['an', 'na', 'ana']

print(find_repeated_substrings("abcdefg"))
# []

print(find_repeated_substrings("abcabcabc"))
# ['ab', 'bc', 'ca', 'abc', 'bca', 'cab', 'abca', 'bcab', 'cabc', 'abcab', 'b]()
