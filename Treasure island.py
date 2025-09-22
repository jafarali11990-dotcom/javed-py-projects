print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right': ")
if choice1 == 'left':
    print("You've come to lake.")
    choice2 = input("There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")
    if choice2 == 'wait':
        print("You arive at the island unharmed.There is house with 3 doors.")
        choice3 = input("Which color do you choose? red, yellow, blue:  ")
        if choice3 == 'red':
            print("It's a room full of fire. Game Over")
        elif choice3 == 'yellow':
            print("You found the treasure! You win!")
        else:
            print("You enter a room of beasts. Game Over")
    else:
        print("You get attacked by an angry trout. Game Over")
else:
    print("You fell into a hole. Game Over")



