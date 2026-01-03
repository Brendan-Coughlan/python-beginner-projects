import random

def roll_dice(num_of_dice : int) -> None:
    roll_list = []
    for _ in range(num_of_dice):
        roll_list.append(random.randint(1, 6))
    
    if num_of_dice == 1:
        print(f"You got a {roll_list[0]}")
    else:
        print(f"You got a {*roll_list,}")

if __name__ == "__main__":
    total_rolls = 0
    while True:
        user_input = input("Roll the dice? (y/n)\n").lower()
        if user_input == "y":
            try:
                num_to_roll = int(input("How many dice?\n"))
            except:
                print("That is a not a number!")
            else:
                if num_to_roll == 0:
                    print("You can't roll 0 dice!")
                else:
                    roll_dice(num_to_roll)
                    total_rolls += num_to_roll
        elif user_input == "n":
            print(f"You rolled a total of {total_rolls} dice. Thank you for your time!")
            break
        else:
            print("Invalid input.")