import random

if __name__ == "__main__":
    print("Welcome to number guessing game!")
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
                print("That isn't a number!")
            else:
                if user_guess == random_num:
                    print("That is correct!")
                    break
                elif user_guess < range_minimum or user_guess > range_maximum:
                    print("That number is not in range! Try again.")
                elif user_guess < random_num:
                    print("Too low! Try again.")
                elif user_guess > random_num:
                    print("Too high! Try again. ")