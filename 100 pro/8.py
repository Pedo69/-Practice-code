from typing import List, Dict
def count_word_occurrences(words: List[str]) -> Dict[str, int]:
    dict = {}
    for i in words:
        dict[i] = words.count(i)
    return dict
        
print(count_word_occurrences(["apple", "banana", "apple", "orange", "banana", "apple"]))