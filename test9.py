def word_frequency(text):
    word = []
    for i in text.split():
        count = text.count(i)
        if i not in word:
            word.append((i, count))
    return word

print(word_frequency("hello world hello, hello Python"))