def word_frequency(text: str) -> dict:
    text = text.lower()
    text = text.replace(".", "").replace(",", "").replace("!", "").replace("?", "")
    words = text.split()

    fre = {}
    for word in words:
        if word in fre:
            fre[word] += 1
        else:
            fre[word] = 1
    return fre
    
print(word_frequency("Hello word! Hello everyone."))
print(word_frequency("This is a test. This teet is easy."))
print(word_frequency("Python is fun. fun fun fun!"))
print(word_frequency("One word, one word."))