from random import randint;
from re import search;

class WordGetter:
    
    @staticmethod
    def supplyWord():
        words = [];
        file = open('text.txt', 'r');
        lines = file.read();
        
        for line in lines.split('\n'):
            for word in line.split():
                words.append(word);
                
        file.close();
        return (words[randint(0, len(words) - 1)]).capitalize();
    
    @staticmethod
    def getWord():
        
        #We want to make sure the word is five characters or above, and contains only letters(could include numbers): we use regex (powerful!)
        word = WordGetter.supplyWord();        
        while len(word) < 5 or search(r'\W+', word) != None: 
            word = WordGetter.supplyWord();
        return word;
        
        