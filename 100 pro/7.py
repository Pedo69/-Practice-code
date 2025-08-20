from typing import List
def collect_unique_words(*words) -> List[str]:
    unique_words = list(dict.fromkeys(words))
    return unique_words

print(collect_unique_words("apple", "banana", "apple", "cherry", "date", "banana", "elderberry"))