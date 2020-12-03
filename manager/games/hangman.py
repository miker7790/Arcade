import os 
import csv
import random


class HANGMAN:
    
    def __init__(self, word=None, attempts=None):
        self.word = word.lower() if word else self._selectRandomWord()
        self.remainingAttempts = attempts if attempts else self._getInitialRemainingAttempts()
        self.remainingLetters = list(self.word)
        self.allGuesses = []
        self.correctGuesses = []
        self.incorrectGuesses = []
        self.lastGuess = None
         
        self._maskWord()
        self._updateGameStatus()                
        

    # sets rules/ initalizes game     
    def playGame(self):
        
        while self.remainingAttempts > 0 and len(self.remainingLetters) > 0:
            print('Unknown Word: {}'.format(self.maskedWord))
            print('Current Available Attempts: {}'.format(self.remainingAttempts))
            
            while True: 
                guess=input('Please guess a single lowercase letter: ')

                if guess and len(guess) == 1 and guess.isalpha() == True:
                    break

            self.lastGuess = guess.lower()       
            self._guessLetter()
            
            for key, item in self.gameStatus.items():
                print('{}: {}'.format(key, item))

            print()
        
        self.gameStatus['word'] = self.word
        self.gameStatus['win'] = True if len(self.remainingLetters) == 0 else False

        message = 'Congrats, the word guessed was: {}' if len(self.remainingLetters) == 0 else 'You lost, you did not guess the word which was: {}'
        print(message.format(self.word), '\n')
        
        return(self.gameStatus)
    

    # updates word after each guess
    def _guessLetter(self):
        
        if self.lastGuess in self.remainingLetters:
            self._correctGuess()   
        elif self.lastGuess not in self.allGuesses:
            self._incorrectGuess()
            
        self.allGuesses.append(self.lastGuess)
        self._updateGameStatus()
            

    # updates word/ records guess        
    def _correctGuess(self):
        
        self.remainingLetters = [i for i in self.remainingLetters if i != self.lastGuess]
        self.correctGuesses.append(self.lastGuess)
        self.remainingAttempts = self.remainingAttempts - 1
        self._maskWord()
        

    # records guess    
    def _incorrectGuess(self):
        
        self.incorrectGuesses.append(self.lastGuess)
        self.remainingAttempts = self.remainingAttempts - 1


    # provides game details as you play   
    def _updateGameStatus(self):
        
        self.gameStatus = {
            'correctGuesses': self.correctGuesses,
            'incorrectGuesses': self.incorrectGuesses,
            'lastGuess': self.lastGuess,     
        }
       

    # masks the word and reveals it for each correct guess
    def _maskWord(self):

        self.maskedWord = ''.join([' _ ' if i in self.remainingLetters else i for i in self.word])


    # selects random word from file of words
    def _selectRandomWord(self):
            
        with open(os.path.dirname(os.path.abspath(__file__)) + '/gameInput/hangman/words.csv') as file:
            words = list(csv.reader(file))
            randomWord = random.choice(words)[0].lower()

        return randomWord


    # initializes the amount of attemps for the game based on the length of the word
    def _getInitialRemainingAttempts(self):

        return len(self.word) + 3