from random import randint

result = "Number too "
game_over = False

while not game_over:
    secret_number = randint(1, 100)
    number_of_guesses = 0
    found = False

    while number_of_guesses < 8 and not found:
        number = int(input("Guess a number between 1 and 100: "))

        if number == secret_number:
            found = True
            print(f"You found the secret number {secret_number} and you guessed {number_of_guesses} time(s)")
        elif number < secret_number:
            print(f"{result} low.")
        else:
            print(f"{result} high.")

        number_of_guesses += 1

    if not found:
        print(f"You were not able to guess the secret number {secret_number}")

    user_input = input("Do you want to play again? ").lower()

    if user_input == "no":
        game_over = True
