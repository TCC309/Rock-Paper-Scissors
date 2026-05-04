import os
import time
import random
 
rules = {"rock":"scissors", "paper":"rock", "scissor":"paper"}

user_input = 0
bot_input = 0

bot_score = 0
user_score = 0

while True:
	user_input = 0
	bot_input = 0

	os.system("cls")
	print(f"Bot: {bot_score}, You: {user_score}")


	user_input = input("rock, paper or scissors?:").lower().replace(" ", "")
	os.system("cls")

	bot_input = random.choice(list(rules))
	
	if user_input not in list(rules):
		os.system("cls")
		print("invalid input")
		time.sleep(1)
		continue

	if bot_input == rules[user_input]:
			user_score += 1
			print("win")
			time.sleep(0.5)
			os.system("cls")
			continue
	elif user_input == bot_input:
			print("monkey")
			time.sleep(0.5)
			os.system("cls")
			continue
	else:
			print("lose")
			time.sleep(0.5)
			bot_score += 1	
			continue