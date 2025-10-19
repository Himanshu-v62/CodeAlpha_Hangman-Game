import random

# Predefined list of words to choose from
word_bank = ["kangaroo", "porcupine", "pineapple", "umbrella", "birthday"]

# Randomly pick a word from the list
correct_word = random.choice(word_bank)

# Create a list of underscores representing the current guessed state
hidden_letters = ["_" for _ in correct_word]

# Keep track of letters the player has already guessed
used_letters = set()

# Limit for wrong guesses
max_attempts = 6
wrong_attempts = 0

print("🎮 Welcome to Hangman Game!")
print("Try to guess the word, one letter at a time.")
print(f"You have 6 incorrect guesses. Let's begin!")

# Main game loop
while wrong_attempts < max_attempts and "_" in hidden_letters:
    print("\nWord: " + " ".join(hidden_letters))
    print(f"Remaining attempts: {max_attempts - wrong_attempts}")
    player_input = input("Guess a letter: ").lower()

    # Input validation
    if not player_input.isalpha() or len(player_input) != 1:
        print("⚠️ Please enter a single alphabet letter.")
        continue

    if player_input in used_letters:
        print("🔁 You already guessed that letter.")
        continue

    used_letters.add(player_input)

    if player_input in correct_word:
        print("✅ Nice! You guessed a correct letter.")
        for index, character in enumerate(correct_word):
            if character == player_input:
                hidden_letters[index] = player_input
    else:
        print("❌ That letter isn't in the word.")
        wrong_attempts += 1

# Game result
if "_" not in hidden_letters:
    print("\n🎉 Well done! You guessed the word:", correct_word)
else:
    print("\n💀 Out of guesses! The word was:", correct_word)
