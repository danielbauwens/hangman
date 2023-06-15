import random
# Importing the random library to be able to randomize the guessing word.

class Hangman:
    def __init__(self):
        # List of attributes
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        ''' Picks a random word from the list and breaks it down into single letters.
        The correct list gets updated to display "_" for every letter in the word'''
        self.word = random.choice(self.possible_words)
        self.word_to_find = []
        for l in self.word:
            self.word_to_find.append(l)
        self.lives = 5
        self.correctly_guessed_letters = list("_"* len(self.word))
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = len(self.wrongly_guessed_letters)

    def play(self):
        '''Method to ask user for their guess.
        Putting the guess into the correct category.
        Lastly increasing the turn counter by 1'''
        guess = input("Please enter a letter to guess:")
        if len(guess) >= 2 or not isinstance(guess, str):
            print("Has to be a letter and cannot be more than one letter. Try again.")
            self.play()
        else:
            for z in self.wrongly_guessed_letters:
                if guess == z:
                    print("You already tried this letter. Try another one.")
                    self.play()
                else:
                    '''Each time a guess goes through, I flag the letter as "False". 
                    Then if it's a match I set it to "True", and this way I can send
                    an output to the wrong letters list and deduct a life when necessary.'''
                    flagletter = False
                    '''This loop checks the guess in relation to the position of the word you're trying to guess.
                    If correct it will put the guess in the correct spot(s).'''
                    for position, letter in enumerate(self.word):
                        if guess.casefold() == letter.casefold():
                            self.correctly_guessed_letters[position] = letter
                            flagletter = True
                        else:
                            continue
                    if flagletter == True:
                        pass
                    else:
                        self.lives -= 1
                        self.wrongly_guessed_letters.append(guess)
                    #Code below only triggered if guess is considered valid. Still part of the "else" condition
                    self.turn_count += 1
                    print(f"Lives remaining: {self.lives}")
                    print(f"Current turn: {self.turn_count}")
                    print(f"It's not these words: {self.wrongly_guessed_letters}")
                    print(f"This is the word you're looking for: {self.correctly_guessed_letters}")

    def game_over(self):
        if self.lives <= 0:
            print("Game over...")

    def well_played(self):
        print(f"You found the word {self.word.upper()} in {self.turn_count} turns with {self.error_count} errors!")
    '''Start loop that continues to play until either the end is triggered (by winning)
    or the game_over attribute called when no lives are available.'''
    def start_game(self):
        the_end = False
        while the_end is False:
            if ''.join(self.correctly_guessed_letters.casefold) == ''.join(self.word_to_find).casefold():
                self.well_played()
                the_end = True
            elif self.lives != 0:
                self.play()
            else:
                self.game_over()
        



        