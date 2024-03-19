from random import sample


def lottery():
    """
        Simulates a lottery game where the player selects 6 unique numbers from a range of 1 to 49.
        The function prompts the player to input their guesses one by one.
        After the player makes their selections, the function generates 6 random numbers as the winning numbers.
        It then compares the player's guesses with the winning numbers to determine if the player has won.

        Returns:
            str: A message indicating the outcome of the lottery game, whether the player has won a prize or not.
        """
    player_guesses = []
    while len(player_guesses) < 6:
        guess = input(f"Enter your number {len(player_guesses) + 1}/6: ")
        try:
            guess = int(guess)
        except ValueError:
            print("It's not a number!")
            continue
        if guess < 1 or guess > 49:
            print("Remember the number should be in range from 1 to 49!")
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
    if 2 < correct_guesses < 6:
        return f"In this draw, you matched {correct_guesses}! Congratulations!"
    elif correct_guesses == 6:
        return f"Congratulations, you've won the jackpot"
    else:
        return "Unfortunately, you didn't win, Try next time!"


print(lottery())
