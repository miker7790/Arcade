from .games import hangman
from .games import tictactoe


class MANAGER:

    def __init__(self):
        self.gameOptions = ['Hangman', 'Tictactoe']
        self.playAgainOptions = ['Yes', 'No']
        self.tracker = {}
        
        self._initiateTracker()
        
    # creates dictionary to track wins/losses
    def _initiateTracker(self):
        
        for gameOption in self.gameOptions:
            self.tracker[gameOption] = {'Wins':0,'Losses':0}

    # initializes manager
    def initiatePlay(self):
        print()
        print("Game Choices:")
        
        for i, game in enumerate(self.gameOptions):
            print('{}. {}'.format(i+1, game))
        
        while True:                     # only allows player to input 1 or 2
            try:
                gameNumber = int(input("Select The Number Of The Game You Want To Play: ")) 
                if gameNumber==1 :
                    print("Loading up hangman...")
                    self.playGame(self.gameOptions[gameNumber-1])
                    break;
                elif gameNumber==2:
                    print("Loading up TicTacToe...")
                    self.playGame(self.gameOptions[gameNumber-1])
                    break;
                else:
                    print("Please select option 1 or 2...")      
            except ValueError:
                print("Provide an integer value...")
                continue
        
        
    # allows option to play again
    def  playAgain(self):               
        print('Would you like to play another game?')
                
        for i, game in enumerate(self.playAgainOptions):
            print('{}. {}'.format(i+1, game))
                    
        while True:
            try:
                gameNumber = int(input("Select an option: ")) 
                if gameNumber==1 :
                    print("Onward! More games lies ahead...")
                    self.initiatePlay()
                    break;
                elif gameNumber==2:
                    self.trackResults()   
                    print("Thank you for playing, goodbye.")
                    break;
                else:
                    print("Please select option 1 or 2...")      
            except ValueError:
                print("Provide an integer value...")
                continue
        
        
    # initializes game/ track results       
    def playGame(self, game):

        if game == 'Hangman':
            x = hangman.HANGMAN().playGame()
            if x['win'] == True:
                self.tracker['Hangman']['Wins'] += 1
            else:
                self.tracker['Hangman']['Losses'] += 1
            self.playAgain()
        
        elif game == 'Tictactoe':
            x = tictactoe.TICTACTOE().playGame()
            if x['win'] == True:
                self.tracker['Tictactoe']['Wins'] += 1
            else:
                self.tracker['Tictactoe']['Losses'] += 1
            self.playAgain()
    
       
    # track/record/calculate results 
    def trackResults(self):
       
        for i in self.gameOptions:
            if self.tracker[i]['Losses']>0:
                self.tracker[i]['Win Ratio'] = float(self.tracker['Hangman']['Wins']/self.tracker['Hangman']['Losses'])
            elif self.tracker[i]['Losses'] == 0 and self.tracker['Hangman']['Wins'] == 0:
                self.tracker[i]['Win Ratio'] = 0
            else:
                self.tracker[i]['Win Ratio'] = 'Infinity'
                
        print()
        print('Would you like to see your record?')
        Options = ['Yes', 'No']
        
        for i, game in enumerate(Options):
                print('{}. {}'.format(i+1, game))
                
        while True:
            try:
                record = int(input("Select one of the options: ")) 
                if record==1 :
                    for i in self.gameOptions:
                        print()    
                        print('Your record for',i, 'is'':')
                        print(self.tracker[i])
                        print()
                    break;
                elif record==2:
                    break;
                else:
                    print("Please select option 1 or 2...")      
            except ValueError:
                print("Provide an integer value...")
                continue
        
        
    def trackStatistics(self):
        print()
    
    
    
        