import random
# Importing the random library to be able to randomize the guessing word.

class Hangman:
    def __init__(self):
        # List of attributes
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word = random.choice(self.possible_words)
        self.word_to_find = []
        self.lives = 5
        self.correctly_guessed_letters = list("_"* len(self.word)) 
        self.wrong = []
        set(self.wrong)
        self.wrongly_guessed_letters = self.wrong
        self.turn_count = 0
        self.error_count = len(self.wrongly_guessed_letters)

        ''' Picks a random word from the list and breaks it down into single letters.
        The correct list gets updated to display "_" for every letter in the word'''
        
        for l in self.word:
            self.word_to_find.append(l)

    def play(self):
        '''Method to ask user for their guess.
        Putting the guess into the correct category.
        Lastly increasing the turn counter by 1'''
        print(f"Lives remaining: {self.lives}")
        print(f"It's not these words: {self.wrongly_guessed_letters}")
        print(f"This is the word you're looking for: {self.correctly_guessed_letters}")
        guess = input("Please enter a letter to guess:")
        if len(guess) >= 2 or not isinstance(guess, str):
            print("Has to be a letter and cannot be more than one letter. Try again.")
            self.play()
        else: 
            for position, letter in enumerate(self.word):
                if guess.casefold() != letter.casefold():
                    self.wrong.append(guess)
                else:
                    self.correctly_guessed_letters[position] = letter
            self.turn_count += 1

    def game_over(self):
        
        self.lives = 0
        print("Game over...")

    def well_played(self):
        print(f"You found the word {self.word.upper()} in {self.turn_count} turns with {self.error_count} errors!")

    def start_game(self):
        while self.lives > 0:
            self.play()
        else:
            self.game_over()
        if self.correctly_guessed_letters is self.word_to_find:
            self.well_played()



        