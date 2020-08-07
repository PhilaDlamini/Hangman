from random import randint;

class WordGuesser:
    
    lives = 3;
    
    @staticmethod
    def start(word):
        print('Welcome to guess the word! You have', WordGuesser.lives, 'lives in total. And the GAME STARTS NOW');
        
        #Replace all the characters in the word with underscores
        currentWord = [];
        for char in word:
            currentWord.append(' _');
        
        #Replace one random underscore with a character
        index = randint(0, len(word) - 1);
        currentWord[index] = word[index];
        
        print('What are the letters in this word:', WordGuesser.__getWord(currentWord));
        
        while WordGuesser.lives > 0:
            
            #Take both the upper and lower parts of this character
            char = input();
            charUpper = char.upper();
            charLower = char.lower();
    
            if (charUpper not in word) and (charLower not in word):
                WordGuesser.lives -= 1;
                print('Letter not in word! You have', WordGuesser.lives, 'lives left');
            else:
                WordGuesser.__replaceUnderScore(charLower, word, currentWord);
                WordGuesser.__replaceUnderScore(charUpper, word, currentWord);
                    
                if (' _' in currentWord): #If we still have underscores, continue guessing
                    print('Continue guessing:', WordGuesser.__getWord(currentWord));  
                else:
                    print('You won! The word was', word);
                
        print('Game over! The word was ', "'" + word + "'", '. You lose hahahahahaha', sep = '');    
        
    #Gets the word from a list of characters
    @staticmethod
    def __getWord(charList):
        word = '';
        for char in charList:
            word += char;
        return word;
    
    @staticmethod
    def __replaceUnderScore(char, word, currentWord):
        try:
            index = word.index(char);
            currentWord[index] = char;
        except:
            return;

        
            
            
            