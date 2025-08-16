from collections import Counter
def word_frequency(text: str) -> dict:
    Result = Counter(text.lower().split())
    return dict(Result)
    
print(word_frequency("Hello word! Hello everyone."))
print(word_frequency("This is a test. This teet is easy."))
print(word_frequency("Python is fun. fun fun fun!"))
print(word_frequency("One word, one word."))