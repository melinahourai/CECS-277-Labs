# 1/28/25
# Purpose: To create a program that will allow the user to play a game of Three Card Monte.
import random
import check_input

def main():
  money = 100 #User starts with $100
  print("-Three Card Monte-")
  print("Find the queen to double your bet!")
  print("You have $" + str(money))
  while money > 0: #While the user still has money, the game will continue
    bet = check_input.get_int_range("How much do you want to bet? ", 1, money)
    if (money < bet):
      print("You don't have enough money!")
    elif (bet < 0): #If the user enters a negative number, the program will                       not continue
      print("You can't bet no money!")
    print("+-----+ +-----+ +-----+")
    print("|     | |     | |     |")
    print("|  1  | |  2  | |  3  |")
    print("|     | |     | |     |")
    print("+-----+ +-----+ +-----+")
    guess = check_input.get_int_range("Find the queen: ", 1, 3)
    queen = random.randint(1, 3) #Generates a random number between 1 and 3
    
    if queen == 1:
      print("+-----+ +-----+ +-----+")
      print("|     | |     | |     |")
      print("|  Q  | |  K  | |  K  |")
      print("|     | |     | |     |")
      print("+-----+ +-----+ +-----+")
    elif queen == 2:
      print("+-----+ +-----+ +-----+")
      print("|     | |     | |     |")
      print("|  K  | |  Q  | |  K  |")
      print("|     | |     | |     |")
      print("+-----+ +-----+ +-----+")
    elif queen == 3:
      print("+-----+ +-----+ +-----+")
      print("|     | |     | |     |")
      print("|  K  | |  K  | |  Q  |")
      print("|     | |     | |     |")
      print("+-----+ +-----+ +-----+")
    if (guess == queen): #If the user guesses the queen correctly, they win                           their bet
      money = money + bet
      print("You won! You have " + str(money) + " dollars!")
    else: #If the user guesses incorrectly, they lose their bet
      money = money - bet
      print("You lost! You have " + str(money) + " dollars left.")
    if money == 0: #If the user runs out of money, the game ends
      print("You have no more money left!")
      break
    yn = check_input.get_yes_no("Play again? (Y/N): ") #Asks the user if they want to play again
    if money != 0:
      if yn:
        continue
      else:
        print("Gameover!")
        break
main()
