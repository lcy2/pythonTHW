class matcher(object):
    def __init__(self, a_len, b_len, pat):
        self.len_dict = {"a": a_len, "b": b_len}
        self.buffer = []
        self.buffer_len = 0
        self.pat_id = 0
        self.pattern = pat
        self.pat_dict = {"a": None, "b": None}
        
    def add_char(self, char):
        self.buffer.append(char)
        self.buffer_len += 1
        
        if self.buffer_len == self.len_dict[self.pattern[self.pat_id]]:
            if not self.pat_dict[self.pattern[self.pat_id]]:
                self.pat_dict[self.pattern[self.pat_id]] = ''.join(self.buffer)
                self.buffer = []
            else:
                if self.pat_dict[self.pattern[self.pat_id]] == ''.join(self.buffer):
                    pass
                else:
                    return False
            self.buffer = []
            self.pat_id += 1
            self.buffer_len = 0
        return True
        
    def __repr__(self):
        return "[" + self.pat_dict.__repr__() + "]"


def match(phrase, pattern):
    pat_len = a_count = 0
    phrase_len = len(phrase)
    matcher_list = []
    
    
    for char in pattern:
        if char == "a":
            a_count += 1
        pat_len += 1
        
    i = 1
    while (i * a_count < phrase_len):
         div, mod = divmod((phrase_len - i * a_count), (pat_len - a_count))
         if (mod == 0 and div != 0):
            matcher_list.append(matcher(i, div, pattern))
         i += 1
    print "last seg"
    
    for char in phrase:
        new_list = []
        for matchr in matcher_list:
            if matchr.add_char(char):
                new_list.append(matchr)
        matcher_list = new_list
        
    
    return True