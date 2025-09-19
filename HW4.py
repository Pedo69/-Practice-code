from collections import defaultdict

def group_by_signature(words: list) -> list:
    groups = defaultdict(list)
    for word in words:
        # use sorted letters of the word as its signature
        signature = "".join(sorted(word))
        groups[signature].append(word)
    return list(groups.values())


if __name__ == "__main__":
    # Example 1
    words = ["abc", "bca", "cab", "bac", "xyz", "yxz", "zxy", "dog"]
    print(group_by_signature(words))
    # Output: [["abc", "bca", "cab", "bac"], ["xyz", "yxz", "zxy"], ["dog"]]

    # Example 2
    words = ["apple", "pale", "leap", "plea", "papel", "hello"]
    print(group_by_signature(words))
    # Output: [["apple", "papel"], ["pale", "leap", "plea"], ["hello"]]
