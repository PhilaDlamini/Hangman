'''Word guesser game. Only issue would be a word with the same repeating characters: e.g eggs. The program
keeps on updating the very first index of g found'''

from WordGetter import WordGetter;
from WordGuesser import WordGuesser;
 
#The main function in this program
def main():
    word = WordGetter.getWord();
    WordGuesser.start(word);

main();