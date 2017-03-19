import string

class word_counter(object):
    def __init__(self, file):
        self.file_dict = {}
        for line in file:
            for word in line.split():
                word = word.lower().translate(None, string.punctuation)
                self.file_dict[word] = self.file_dict.setdefault(word, 0) + 1
                
    def get_word_count(self, word):
        word = word.lower()
        return self.file_dict.setdefault(word, 0)