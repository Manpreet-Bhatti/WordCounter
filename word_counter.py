import sys # Importing the ability to use the command line to input text files
import string # Imported to use the punctuation feature

class countWords:
    def __init__(self, file_new):
        self.file_new = file_new

    def count_the_words(self): # Counts the total amount of words
        bunch_of_words = self.file_new.split(" ")
        amount_of_words = len(bunch_of_words)
        return amount_of_words

    def most_common(self): # Counts and prints the most common words in (word, count) format
        for p in string.punctuation:  # Cleans the punctuation
            self.file_new = self.file_new.replace(p, " ")

        new_words = self.file_new.lower().split()
        
        lone = set()  # Set of unique words
        for w in new_words:
            lone.add(w)
        
        pairs = []  # List of (count, unique) tuples
        for l in lone:
            count = 0
            for w in new_words:
                if w == l:
                    count += 1
            pairs.append((count, l))
        
        pairs.sort()  # Sort the list
        pairs.reverse()  # Reverse it, making highest count first
        
        for i in range(min(10, len(pairs))):  # Print the ten most frequent words
            count, word = pairs[i]
            print("%s: %d" %(word, count))

if __name__ == "__main__": # Run code below if a text file is inputted
    if len(sys.argv) < 2:
        print("Usage: python word_count.py <file name>.txt")
        exit(1)

filename = sys.argv[1]

f = open(filename, "r")
file_read = f.read()
f.close()

file_data = countWords(file_read)

file_data.most_common()

num_of_words = file_data.count_the_words()
print("The total number of words are: %d" %(num_of_words))
