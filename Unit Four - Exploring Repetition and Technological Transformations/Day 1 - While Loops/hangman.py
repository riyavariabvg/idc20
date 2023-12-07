import random

def choose_word():
    word_list = ['apple', 'banana', 'orange', 'grape', 'melon', 'strawberry', 'peach']
    return random.choice(word_list)

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + ' '
        else:
            displayed_word += '_ '
    return displayed_word

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")


        if guess in guessed_letters:
            print("You've already guessed that letter.")

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print("Incorrect!")
            print(f"Attempts left: {attempts}")
            if attempts == 0:
                print("Sorry, you ran out of attempts! The word was:", word_to_guess)
                break
        else:
            print("Correct!")

        word_display = display_word(word_to_guess, guessed_letters)
        print(word_display)

        if '_' not in word_display:
            print("Congratulations! You've guessed the word:", word_to_guess)
            break

hangman()
