from Bai5_1 import s1, s2
words = (s1 + " " + s2).split()
unique_words = list(dict.fromkeys(words))
vocab = {}
for idx, word in enumerate(unique_words):
    vocab[word] = idx
print(words)