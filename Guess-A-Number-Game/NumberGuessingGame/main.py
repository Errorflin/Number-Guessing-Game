import random ## // import random to generate random numbers

random_num = random.randint(1, 100) ## // random num from 1 - 100 so player can guess
print("GUESS THE NUMBER") ## // title of the game

def main(): ## // define main "game"
	player_num = input("> ") ## // input "> "

	if int(player_num) > int(random_num): ## // checks if number choosed by player is grater than random number
		print("Too big.")
		main() ## // call a function from scratch but player knows that his number was too big

	elif int(player_num) < int(random_num): ## // checks if number choosed by player is less than random number
		print("Too small.")
		main() ## // call a function from scratch but player knows that his number was too small

	elif int(player_num) == int(random_num): ## // checks if player guesed correctly
		print("YOU GUESSED CORRECTLY !")

main() ## // run the program (main())
