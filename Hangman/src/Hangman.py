'''
Hangman.py
Diwas Poudel
Homework 2
'''

import sys
import random
from itertools import groupby
from multiprocessing.connection import families
from curses.ascii import isdigit

class Hangman:
    '''
    Initializes the words list
    '''
    def __init__(self):
        file = open('words.txt','r')
        self.words = []
        self.wordguess = []
        self.lengthWords =[]
        self.win = False
        
        for line in file:
            self.words.append(line.rstrip())
        
            
    '''
    Outputs the current status of the guesses
    '''
        
    def printword(self):
        for c in self.wordguess:
            print c,
        print

    def playgame(self):
        #generate random word
        wordFound = False
        while wordFound != True:
            userLength = raw_input('Enter length of word (more than 3):')
            
            if userLength.isdigit():
                userLength = int(userLength)
                if userLength >3:  
                    if (wordFound == False):              
                        for wording in self.words:
                            if(len(wording) == userLength):
                                self.lengthWords.append(wording)
                                wordFound = True 
                    else:
                        print "No word of the length " + str(userLength)
                        break     
                else:
                    print "Please enter value more than 3" 
            else:
                print "Please enter digit value"
            
        if wordFound:
            word = self.lengthWords[random.randint(0,len(self.lengthWords)-1)]
            self.wordguess = ['_'] * len(word)
            isDigit = False
            while (isDigit!= True):
                userGuess = raw_input('Enter number of guess you want:')
                if userGuess.isdigit():
                    isDigit = True
            userGuess = int(userGuess)
            guesses = 0
            self.guessedLetter = []       
                            
            while guesses<=userGuess:
                if guesses < userGuess:
                    if "_" not in self.wordguess:
                        print "Congratulations, you completed the evil hangman"
                        break
                    else: 
                        ch = raw_input('Enter a guess:').lower()
                        if ch not in self.guessedLetter:
                            if ch.isalpha():
                                family ={}
                                for word in self.lengthWords:
                                    key = ' '.join(ch if c == ch else '_' for c in word)
                                    if key not in family:
                                        family[key] = []
                                    family[key].append(word)
                                self.lengthWords = max(family.values(), key=len)
                                
                                for sortedWords in self.lengthWords:
                                    if ch not in sortedWords:
                                         print ch + " does not occur"      
                                         break
                                    else:
                                        letterTimes = map(lambda letter : letter == ch, sortedWords)    
                                        for status in letterTimes:
                                            if status:
                                                self.wordguess[letterTimes.index(status)] = ch  
                                                letterTimes[letterTimes.index(status)] = False
                                        for p in self.wordguess: 
                                            print p,
                                        print
                                        break           
                            else:
                                print "Only allow alphabetic characters."        
                        else:
                            print "The letter " + ch + " has already been used."
                else:
                    print "Sorry dude, the word is " + random.choice(self.lengthWords)
                    break
                guesses += 1
                self.guessedLetter.append(ch) 
                

if __name__ == "__main__":

    game = Hangman()

    game.playgame()
    
    
