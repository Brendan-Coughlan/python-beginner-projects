import random

if __name__ == "__main__":
    guesses_left = 3
    print(f"Welcome to number guessing game! You have {guesses_left} guesses to answer the question!")
    try:
        range_minimum = int(input("Minimum: "))
        range_maximum = int(input("Maximum: "))
    except:
        print("That is not a number!")
    else:
        random_num = random.randint(range_minimum, range_maximum)
        while True:
            try:
                user_guess = int(input(f"Guess the number between {range_minimum} and {range_maximum}: ") )
            except:
                print("That isn't a number! You aren't penalized. Try again.")
            else:
                if user_guess == random_num:
                    print("That is correct!")
                    break
                elif user_guess < range_minimum or user_guess > range_maximum:
                    print("That number is not in range! You aren't penalized. Try again.")
                elif user_guess < random_num:
                    guesses_left -= 1

                    if guesses_left == 0:
                        print(f"You are out of guesses! The corrent answer was {random_num}. Better luck next time.")
                        break

                    print(f"Too low! You have {guesses_left} guesses left. Try again.")
                elif user_guess > random_num:
                    guesses_left -= 1

                    if guesses_left == 0:
                        print(f"You are out of guesses! The corrent answer was {random_num}. Better luck next time.")
                        break

                    print(f"Too high! You have {guesses_left} guesses left. Try again.")