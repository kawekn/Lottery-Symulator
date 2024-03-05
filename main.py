from random import sample


def lottery():
    player_guesses = []
    while len(player_guesses) < 6:
        guess = input(f"Enter your number {len(player_guesses) + 1}/6: ")
        try:
            guess = int(guess)
        except ValueError:
            print("It's not a number!")
            continue
        if guess < 1 or guess > 49:
            print("Remember the number should be in range from 1 to 49")
            continue
        elif guess in player_guesses:
            print("Remember numbers should be unique!")
        else:
            player_guesses.append(guess)

    player_guesses.sort()
    print(f"Numbers You have chosen: {player_guesses}")
    winning_numbers = sample(range(1, 50), 6)
    print(f"Drawn numbers are: {winning_numbers}")
    correct_guesses = 0

    for number in winning_numbers:
        for attempt in player_guesses:
            if attempt == number:
                correct_guesses += 1
    if correct_guesses > 2:
        return f"You win with score {correct_guesses}/6"
    else:
        return "You lose, Try next time!"


print(lottery())
