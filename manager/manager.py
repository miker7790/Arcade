from .games import hangman
from .games import tictactoe


class MANAGER:

    def __init__(self):
        self.gameMapping = {'Hangman': hangman.HANGMAN(), 'TicTactoe': tictactoe.TICTACTOE()}
        self.binaryOptions = ['Yes', 'No']
        self.gamesPlayed = 0
        self.playAgain = True
        self.gameSelectionMessage = 'Select The Number Of The Game You Want To Play: '
        self.playAgainSelectionMessage = 'Select The Number To Decide Whether To Play Again: '
        self.displayResultsSelectionMessage = 'Select The Number To Decide Whether To View Results: '
        self.incorrectSelectionMessage = 'Please select an integer between 1-{}'
        
        self._initializeSetup()


    # create list of game options and dictionary to track wins/losses
    def _initializeSetup(self):

        self.gameOptions = [key for key in self.gameMapping]
        self.tracker = {gameOption: {'Wins':0, 'Losses':0} for gameOption in self.gameOptions}


    # reusable selection options function
    def _displaySelectionOptions(self, items):

        for i, item in enumerate(items):
            print('{}. {}'.format(i+1, item))

    
    # reusable check correct selection function
    def _checkCorrectSelection(self, selectionMessage, items):

        selection = input(selectionMessage)

        try:
            selection = int(selection)

            if selection in range(1, len(items)+1):
                return selection

        except:
            pass

        print(self.incorrectSelectionMessage.format(len(items)))

        return False


    # initiate game selection
    def _initiateGameSelection(self):

        print('\nGame Choices:')
        self._displaySelectionOptions(items=self.gameOptions)

        while True:
                
            selection = self._checkCorrectSelection(selectionMessage=self.gameSelectionMessage, items=self.gameOptions)

            if selection:
                return selection
            

    # initiate play again selection
    def _initiatePlayAgainSelection(self):

        print('\nWould you like to play another game?')
        self._displaySelectionOptions(items=self.binaryOptions)

        while True:
            
            selection = self._checkCorrectSelection(selectionMessage=self.playAgainSelectionMessage, items=self.gameOptions)

            if selection:
                print('Onward! More games lies ahead...') if selection == 1 else print('Thank you for playing, goodbye.')
                self.playAgain = True if selection == 1 else False
                    
                return


    # initializes manager
    def initiatePlay(self):

        while self.playAgain:

            if self.gamesPlayed > 0:
                self._initiatePlayAgainSelection()

            if self.playAgain:
                gameNumber = self._initiateGameSelection()
                print('Loading up {}...'.format(self.gameOptions[gameNumber-1]))
                self.playGame(game=self.gameOptions[gameNumber-1])

        self._displayResults()
        
        
    # initializes game/ track results       
    def playGame(self, game):

        x = self.gameMapping[game].playGame()

        if x['win'] == True:
            self.tracker[game]['Wins'] += 1
        else:
            self.tracker[game]['Losses'] += 1

        self.gamesPlayed += 1
    
       
    # track/record/calculate results 
    def _displayResults(self):
                
        print('\nWould you like to see your record?')
        self._displaySelectionOptions(items=self.binaryOptions)
                
        while True:
            selection = self._checkCorrectSelection(selectionMessage=self.displayResultsSelectionMessage, items=self.gameOptions)
                
            if selection:
                                
                if selection==1:
                    print()
                    for i in self.gameOptions:
                        print('Your record for', i, 'is:', self.tracker[i])

                return