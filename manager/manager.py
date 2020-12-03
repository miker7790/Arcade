from .games import hangman
from .games import tictactoe


class MANAGER:

    def __init__(self):
        self.gameMapping = {'Hangman': hangman.HANGMAN(), 'TicTactoe': tictactoe.TICTACTOE()}
        self.binaryOptions = ['Yes', 'No']
        self.gamesPlayed = 0
        self.playAgain = True
        self.gameSelectionIntroductionMessage = 'Game Choices:'
        self.gameSelectionMessage = 'Select The Number Of The Game You Want To Play: '
        self.loadingGameMessage = 'Loading up {}...'
        self.playAgainIntroductionMessage = 'Would you like to play another game?'
        self.playAgainSelectionMessage = 'Select The Number To Decide Whether To Play Again: '
        self.playAgainYesMessage = 'Onward! More games lies ahead...'
        self.playAgainNoMessage = 'Thank you for playing, goodbye.'
        self.displayResultsIntroductionMessage = 'Would you like to see your record?'
        self.displayResultsSelectionMessage = 'Select The Number To Decide Whether To View Results: '
        self.displayResultsMessage = 'Your record for {} is: {}'
        self.incorrectSelectionMessage = 'Please select an integer between 1-{}'
        
        self._initializeSetup()


    # create list of game options and dictionary to track wins/losses
    def _initializeSetup(self):

        self.gameOptions = [key for key in self.gameMapping]
        self.tracker = {gameOption: {'win':0, 'loss':0, 'played':0} for gameOption in self.gameOptions}


    # reusable selection options function
    def _displaySelectionOptions(self, selectionIntroductionMessage, items):

        print()
        print(selectionIntroductionMessage)

        for i, item in enumerate(items):
            print('{}. {}'.format(i+1, item))

        print()

    
    # reusable check correct selection function
    def _checkCorrectSelection(self, selectionMessage, items):

        try:
            selection = input(selectionMessage)
            selection = int(selection)

            if selection in range(1, len(items)+1):
                return selection

        except:
            pass

        print(self.incorrectSelectionMessage.format(len(items)))

        return False


    # initiate game selection
    def _initiateGameSelection(self):

        self._displaySelectionOptions(selectionIntroductionMessage=self.gameSelectionIntroductionMessage, items=self.gameOptions)

        while True:
            selection = self._checkCorrectSelection(selectionMessage=self.gameSelectionMessage, items=self.gameOptions)

            if selection:
                return selection
            

    # initiate play again selection
    def _initiatePlayAgainSelection(self):

        self._displaySelectionOptions(selectionIntroductionMessage=self.playAgainIntroductionMessage, items=self.binaryOptions)

        while True:
            selection = self._checkCorrectSelection(selectionMessage=self.playAgainSelectionMessage, items=self.gameOptions)

            if selection:
                print(self.playAgainYesMessage) if self.binaryOptions[selection-1]=='Yes' else print(self.playAgainNoMessage)
                self.playAgain = True if self.binaryOptions[selection-1]=='Yes' else False
                    
                return


    # track/record/calculate results 
    def _initiateResultsSelection(self):

        self._displaySelectionOptions(selectionIntroductionMessage=self.displayResultsIntroductionMessage, items=self.binaryOptions)
                
        while True:
            selection = self._checkCorrectSelection(selectionMessage=self.displayResultsSelectionMessage, items=self.binaryOptions)
                
            if selection:
                                
                if self.binaryOptions[selection-1]=='Yes':
                    print()
                    for i in self.gameOptions:
                        print(self.displayResultsMessage.format(i, self.tracker[i]))

                return


    # initializes manager
    def initiatePlay(self):

        while self.playAgain:

            if self.gamesPlayed > 0:
                self._initiatePlayAgainSelection()

            if self.playAgain:
                gameNumber = self._initiateGameSelection()
                print(self.loadingGameMessage.format(self.gameOptions[gameNumber-1]))
                self.playGame(game=self.gameOptions[gameNumber-1])

        self._initiateResultsSelection()
        
        
    # initializes game/ track results       
    def playGame(self, game):

        x = self.gameMapping[game].playGame()
        self.tracker[game]['played'] += 1
        self.tracker[game]['win'] += 1 if x['win'] else 0
        self.tracker[game]['loss'] = self.tracker[game]['played'] - self.tracker[game]['win']
        self.gamesPlayed += 1