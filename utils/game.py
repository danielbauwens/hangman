import random
# Importing the random library to be able to randomize the guessing word.


class hangman:
    def __init__(self):
        # List of attributes
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = []
        self.lives = 5
        self.correctly_guessed_letters = []
        self.wrongly_guessed_letters = {}
        self.turn_count = 0
        self.error_count = len(self.wrongly_guessed_letters)
        self.guessed_letters = guess
        ''' Picks a random word from the list and breaks it down into single letters.
        The correct list gets updated to display "_" for every letter in the word'''
        self.word = random.choice(self.possible_words)
        for letter in self.word:
            self.word_to_find.append(letter)
            self.correctly_guessed_letters.append("_")

    def play(self):
        '''Method to ask user for their guess.
        Putting the guess into the correct category.'''
        guess = str(input("Please enter a letter to guess:"))
        if len(guess) >= 2:
            hangman.play()
            print("Cannot be more than one letter. Try again.")
        else: 
            
            for i in self.word:
                if guess.casefold() != i.casefold():
                    self.wrongly_guessed_letters + i 
                else:
                    self.correctly_guessed_letters.append(i)

    def game_over(self):
        self.lives = 0
        print("Game over...")

    def well_played(self):
        print(f"You found the word {self.word.upper()} in {self.turn_count} turns with {self.error_count} errors!")

    def start_game(self):
        while lives > 0:
            hangman.play()
        else:
            self.game_over()
        if self.correctly_guessed_letters is self.word_to_find:
            self.well_played()



        