def count_word_repetition(text):
    words = text.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

my_string = "hello world hello"
word_counts = count_word_repetition(my_string)
print(word_counts)
# Output: {'hello': 2, 'world': 1}