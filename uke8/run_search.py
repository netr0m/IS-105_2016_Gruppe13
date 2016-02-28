import Search

class SearchLetter(Search.Search):
    def __init__(self, filename, bazinga):
        self.bazinga = bazinga                      # Looking for the word 'bazinga'
        self.fileName = filename                    # Which file we're looking in
        input_file = open(self.fileName, 'r')
        self.prepare = input_file.read()
        input_file.close()
        pass
    
class SearchWord(Search.Search):
    def __init__(self, filename, bazinga):
        self.bazinga = bazinga
        self.fileName = filename
        input_file = open(self.fileName, 'r')
        self.prepare = input_file.read().split()
        input_file.close()
        pass
    

def run():
    # For every letter
    print ("For each letter")
    search_letters = SearchLetter(
    'gruppe.txt',                                   # Filename
    'bazinga')                                      # The word we're looking for (bazinga)
    
    search_letters.run_search(10)
    
    print
    
    print ("For each word")
    # For each word
    search_words = SearchWord(
    'gruppe.txt',
    'bazinga')
    
    search_words.run_search(10)
    
if __name__ == '__main__':
    run()