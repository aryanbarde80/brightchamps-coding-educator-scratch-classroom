from random import randint


def read_guess():
    """Read a valid number from the player."""
    while True:
        user_input = input("Enter your guess from 1 to 20: ")
        if user_input.isdigit():
            return int(user_input)
        print("Please type a number only.")


def play_game():
    secret_number = randint(1, 20)
    attempts = 0
    max_attempts = 6

    print("Welcome to Number Quest!")
    print("I am thinking of a number between 1 and 20.")

    while attempts < max_attempts:
        guess = read_guess()
        attempts += 1

        if guess == secret_number:
            print(f"Correct! You found it in {attempts} attempts.")
            return
        if guess < secret_number:
            print("Too low. Try a bigger number.")
        else:
            print("Too high. Try a smaller number.")

        print(f"Attempts left: {max_attempts - attempts}")

    print(f"Game over. The secret number was {secret_number}.")


if __name__ == "__main__":
    play_game()

