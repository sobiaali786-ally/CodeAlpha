import random

# -----------------------------------------------
# TASK 1: Hangman Game
# Key Concepts: random, while loop, if-else, strings, lists
# -----------------------------------------------

# Step 1: Predefined word list (5 words, no file/API needed)
word_list = ["python", "hangman", "coding", "laptop", "github"]

# Step 2: Randomly pick a word
secret_word = random.choice(word_list)

# Step 3: Setup game variables
max_wrong_guesses = 6
wrong_guesses = 0
guessed_letters = []

# Step 4: Create display (underscores for each letter)
def get_display(word, guessed):
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

# Step 5: Hangman ASCII art stages
hangman_stages = [
    # 0 wrong
    """
       ------
       |    |
       |
       |
       |
       |
    --------""",
    # 1 wrong
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------""",
    # 2 wrong
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------""",
    # 3 wrong
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------""",
    # 4 wrong
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------""",
    # 5 wrong
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------""",
    # 6 wrong - DEAD
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------""",
]

print("=" * 40)
print("       WELCOME TO HANGMAN GAME!")
print("=" * 40)
print(f"Hint: The word has {len(secret_word)} letters.\n")

# Step 6: Main game loop
while wrong_guesses < max_wrong_guesses:
    print(hangman_stages[wrong_guesses])
    print(f"\nWord: {get_display(secret_word, guessed_letters)}")
    print(f"Wrong guesses left: {max_wrong_guesses - wrong_guesses}")
    print(f"Letters guessed: {', '.join(guessed_letters) if guessed_letters else 'None'}")

    # Check if player won
    if all(letter in guessed_letters for letter in secret_word):
        print("\n🎉 CONGRATULATIONS! You guessed the word:", secret_word.upper())
        break

    # Get player input
    guess = input("\nEnter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single letter only!")
        continue

    if guess in guessed_letters:
        print(f"⚠️  You already guessed '{guess}'. Try a different letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in secret_word:
        print(f"✅ Good guess! '{guess}' is in the word.")
    else:
        wrong_guesses += 1
        print(f"❌ Wrong! '{guess}' is not in the word.")

# Step 7: Game over check
else:
    print(hangman_stages[wrong_guesses])
    print(f"\n💀 GAME OVER! The word was: {secret_word.upper()}")

print("\nThanks for playing Hangman!")
print("=" * 40)
