import os


def convert_int(int_str):
    try:
        return int(int_str)
    except (ValueError):
        return None

def scan(sentence):
    tokens = load_tokens()
    result = []
    
    words = sentence.split()
    for word in words:
        if word.lower() in tokens:
            result.append((tokens[word], word.lower()))
        elif convert_int(word) != None:
            result.append(('number', int(word)))
        else:
            result.append(('error', word))
    return result
    
def load_tokens():
    tokens = dict()
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    
    with open(os.path.join(__location__, "tokens.txt")) as f:
        for line in f:
            word, type = line.split()
            tokens[word] = type
    return tokens