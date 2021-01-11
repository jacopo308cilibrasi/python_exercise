#Print the revese on the console!

word = input("Gimme a word:")

reverse = ''

word_len = len(word) -1

while word_len >= 0:
    reverse = reverse + word[word_len]
    word_len = word_len - 1

print(reverse)
    
