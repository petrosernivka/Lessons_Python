#https://www.codewars.com/kata/interactive-dictionary
class Dictionary():
    def __init__(self):
        self.d = {}
    def newentry(self, word, definition):
        self.d[word] = definition
    def look(self, word):
        return self.d[word] if word in self.d else '''Can't find entry for ''' + word
