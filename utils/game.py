import random
# Importing the random library to be able to randomize the guessing word.

class Hangman:
    def __init__(self):
        # List of attributes
        # Picks a random word from the list and breaks it down into single letters.
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word = random.choice(self.possible_words)
        #The correct list gets updated to display "_" for every letter in the word
        self.word_to_find = []
        for l in self.word:
            self.word_to_find.append(l)
        
        self.correctly_guessed_letters = list("_"* len(self.word))

        # Convert list into a set and back into a list to avoid duplicate values.
        self.wrongly_guessed_letters = []
        self.oopsie = list(set(self.wrongly_guessed_letters))

        # Set starting values.
        self.lives = 5
        self.turn_count = 0
        self.error_count = 0

    def play(self):
        # Asks the players to input a letter guess.
        guess = input("\nPlease enter a letter to guess:")
        # Resets a bool value to use for an "if" condition that checks if it's a valid input.
        good_guess = True
        # Checks if it's a recurring wrong guess and notifies the player.
        if guess in self.wrongly_guessed_letters:
            print("\nYou already tried this letter. Try another one!")
            good_guess = False
            self.play()

        # Checks if it's a recurring right guess and notifies the player.
        elif guess in self.correctly_guessed_letters:
            print("\nYou already tried this letter succesfully. Find the next one!")
            self.play()

        # Checks for a single letter that is a string and part of the alphabet and notifies the player.
        if len(guess) >= 2 or not isinstance(guess, str) or not guess.isalpha():
            print("\nHas to be a letter and cannot be more than one letter. Try again!\n")
            self.play()

        elif len(guess) < 2 and isinstance(guess, str) and good_guess == True:

            # If bool is True I know not to update the wrong_letters list. 
            flagletter = False

            # Checks position and letter of winning word and if there's a match with player guess, add it to the correct list.
            for position, letter in enumerate(self.word):
                if guess.casefold() == letter.casefold():
                    self.correctly_guessed_letters[position] = letter
                    flagletter = True
                else:
                    continue
            # Checks with previous bool values to determine if letter was right or wrong.
            if flagletter == True or good_guess == False:
                pass
            else:
                self.lives -= 1
                self.wrongly_guessed_letters.append(guess)
                self.oopsie = list(set(self.wrongly_guessed_letters))

            # End of turn code is only triggered if guess is considered valid.
            self.turn_count += 1
            self.error_count = len(self.oopsie)
            print(f"\nLives remaining: {self.lives}")
            print(f"Current turn: {self.turn_count}")
            print(f"It's not these words: {self.oopsie}")
            print(f"This is the word you're looking for: {self.correctly_guessed_letters}")
        
    # Checks if lives is at 0 and presents the "Game Over" text.
    def game_over(self):
        if self.lives <= 0:
            print(f"Game over! The word was {self.word.upper()}!")

    # If your word matches the winning word it congratulates you with the game stats.
    def well_played(self):
        print(f"You found the word {self.word.upper()} in {self.turn_count} turns with {self.error_count} errors!")
    
    # Start loop that continues to play until either the end is triggered (by winning)
    # or the "game_over" method is called when no lives are available.
    def start_game(self):
        the_end = False
        while the_end is False:
            # Checks to see if word matches the winning word.
            if ''.join(self.correctly_guessed_letters).casefold() == ''.join(self.word_to_find).casefold():
                self.well_played()
                the_end = True
            
            # While "the_end" is still False and your lives are above 0 continues to call Play.
            elif self.lives != 0:
                self.play()
            # If conditions not met, ends the game.
            else:
                self.game_over()
                the_end = True
