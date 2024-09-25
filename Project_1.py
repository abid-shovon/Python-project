"""
Russel_viper = -1
Tik_Toker = 0
Gun = 1
"""

import random

item_list = {"Russel_Viper": -1, "Tik_Toker": 0, "Gun": 1}
reversed_item_list = {-1: "Russel_Viper", 0: "Tik_Toker", 1: "Gun"}

def funny_game(value):
    try:
        computer = random.choice([-1, 0, 1])

        print(f"Computer choice: {reversed_item_list[computer]}")
        print(f"User choice: {reversed_item_list[value]}")

        if computer == value:
            print("You and computer made the same choice, so the game is a draw!")
        else:
            if computer == -1 and value == 0:
                print("Win Russel_Viper")
            elif computer == -1 and value == 1:
                print("Lose Russel_Viper")
            elif computer == 0 and value == 1:
                print("Ticktoker win Cause We can't Kill a Human-being")
            elif computer == 0 and value == -1:
                print("Win  Russel_Viper")
            elif computer == 1 and value == -1:
                print("Lose Russel_Viper")
            elif computer == 1 and value == 0:
                print("Ticktoker win Cause We can't Kill a Human-being")
            else:
                print("There are some problem in code please check")
    except KeyError:
        print("Invalid input. Please enter -1, 0, or 1.")



while True:
    try:
        user_input = int(input("Choose an item (enter -1 for Russel_Viper, 0 for Tik_Toker, 1 for Gun): "))
        funny_game(user_input)
    except ValueError:
        print("Invalid input. Please enter an integer.")

