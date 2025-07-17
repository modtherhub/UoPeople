# improve the function by converting all words to lowercase and removing punctuation to ensure accuracy.
import string

def word_frequency(text):
    text = text.lower()
    for char in string.punctuation:
        text = text.replace(char, "")
    
    words = text.split()
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq

print(word_frequency("Hello, world! Hello again."))