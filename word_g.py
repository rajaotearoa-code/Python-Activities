import random
import string


class WordGuessingGame:
    """
    A class representing the Word Guessing CLI game.
    Encapsulates the game state (word, blanks, remaining lives, used letters)
    and game logic methods into a single object.
    """

    def __init__(self, max_lives=6):
        """Initializes the game state and attributes."""
        # Predefined pool of words
        self.word_list = [
            "python", "variable", "function", "iterator", "notebook",
            "pipeline", "dataset", "computer", "research", "analytics"
        ]
        
        # State tracking attributes
        self.max_lives = max_lives
        self.lives = max_lives
        self.used_letters = set()
        
        # Select secret word and build matching blanks list
        self.secret_word = self._get_random_word()
        self.blanks = ["_" for _ in self.secret_word]

    def _get_random_word(self):
        """Selects a random target word from the word list."""
        return random.choice(self.word_list)

    def _prompt_for_letter(self):
        """
        Prompts the user for input and validates that it is a single,
        previously unused A-Z letter.
        """
        while True:
            guess = input("Guess a letter: ").strip().lower()
            
            # Validate input length and alphabetical character
            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print(" → Please enter a single A-Z letter.")
                continue
            
            # Check if letter was already attempted
            if guess in self.used_letters:
                print(" → You already tried that letter.")
                continue
            
            return guess

    def _reveal_letters(self, letter):
        """
        Checks if the guessed letter exists in the secret word
        and updates the blanks list accordingly.
        """
        found_any = False
        for i, ch in enumerate(self.secret_word):
            if ch == letter and self.blanks[i] == "_":
                self.blanks[i] = letter
                found_any = True
        return found_any

    def _all_blanks_filled(self):
        """Returns True if no underscore '_' remains in the blanks list."""
        return "_" not in self.blanks

    def play(self):
        """Starts and manages the main game loop execution."""
        print("\nWelcome to Word Guessing!")
        print(f"The word has {len(self.secret_word)} letters.")
        print(" ".join(self.blanks))

        while True:
            # 1. Get a valid letter guess from the user
            guess = self._prompt_for_letter()
            self.used_letters.add(guess)

            # 2. Check if guess matches any letters in the secret word
            if self._reveal_letters(guess):
                print("\n Well done, Nice job! You found a letter.")
                print(" ".join(self.blanks))
                
                # Check for win condition
                if self._all_blanks_filled():
                    print("\n Congratulation! You guessed the word!")
                    print(f"Word: {self.secret_word}")
                    print("GAME OVER")
                    break
            else:
                # Deduct life on incorrect guess
                self.lives -= 1
                print(f"\nNope. You lose a life. Lives left: {self.lives}")
                print(" ".join(self.blanks))

                # Check for loss condition
                if self.lives <= 0:
                    print("\n Out of lives & Sad story!")
                    print(f"The word was: {self.secret_word}")
                    print("GAME OVER")
                    break


# Entry point of execution
if __name__ == "__main__":
    # Create an instance of the game object and launch it
    game = WordGuessingGame(max_lives=6)
    game.play()