from colorama import Fore, Back, Style
import random
print(Fore.BLUE + 'Rock-paper-scissors \u00A92022'), print('V 1.0')
print(Fore.WHITE + 'Rock-paper-scissors made by HydroApps [https://github.com/hydroapps]')
print(Fore.GREEN + """This program comes with ABSOLUTELY NO WARRANTY; for details refer 'LICENSE.md'.
    This is free software, and you are welcome to redistribute it under certain conditions;refer 'LICENSE.md' for details.""")
print(Fore.WHITE  + """Refer 'Readme' file for solutions of some common issues
You are free to contact me :
  Discord:Loki_Laufeyson#2473 
  Telegram:https://t.me/Loki_Laufeyson_2473 
if you find more issues/errors. """)

print(Fore.YELLOW + "Winning Rules of the Rock paper scissor game are as follows: \n"
								+"Rock vs paper->paper wins \n"
								+ "Rock vs scissor->Rock wins \n"
								+"paper vs scissor->scissor wins \n")

while True:
	print(Fore.MAGENTA + "Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")
	
	# take the input from user
	choice = int(input(Fore.WHITE +"User turn: "))
	
	# looping until user enter invalid input
	while choice > 3 or choice < 1:
		choice = int(input("enter valid input: "))
		

	# initialize value of choice_name variable
	# corresponding to the choice value
	if choice == 1:
		choice_name = 'Rock'
	elif choice == 2:
		choice_name = 'paper'
	else:
		choice_name = 'scissor'
		
	# print user choice
	print("user choice is: " + choice_name)
	print("\nNow its computer turn.......")

	# Computer chooses randomly any number
	# among 1 , 2 and 3. Using randint method
	# of random module
	comp_choice = random.randint(1, 3)
	
	# looping until comp_choice value
	# is equal to the choice value
	while comp_choice == choice:
		comp_choice = random.randint(1, 3)

	# initialize value of comp_choice_name
	# variable corresponding to the choice value
	if comp_choice == 1:
		 comp_choice_name = 'Rock'
	elif comp_choice == 2:
		comp_choice_name = 'paper'
	else:
		comp_choice_name = 'scissor'
		
	print("Computer choice is: " + comp_choice_name)

	print(choice_name + " V/s " + comp_choice_name)

	
	if((choice == 1 and comp_choice == 2) or
	(choice == 2 and comp_choice ==1 )):
		print("paper wins => ", end = "")
		result = "paper"
		
	elif((choice == 1 and comp_choice == 3) or
		(choice == 3 and comp_choice == 1)):
		print("Rock wins =>", end = "")
		result = "Rock"
	else:
		print("scissor wins =>", end = "")
		result = "scissor"

	# Printing either user or computer wins
	if result == choice_name:
		print(Fore.RED + "<== User wins ==>")
	else:
		print(Fore.RED + "<== Computer wins ==>")
		
	print(Fore.WHITE + "Do you want to play again? (Y/N)")
	ans = input()


	# if user input n or N then condition is True
	if ans == 'n' or ans == 'N':
		break
	
# after coming out of the while loop
# we print thanks for playing
print("\nThanks for playing")
k=input("press Enter to close or exit")

