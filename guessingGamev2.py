#!/bin/bash/python3

import random

guesses = [0]
num = random.randint(1,100)

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

while True:
	guesses.append(int(input('Guess the number:\n')))

	if guesses[-1]==num:
		print(f'You are correct, the number is {num}. You got it in {len(guesses)} tries')
		break
	else:
		if guesses[-2]:
			if abs(guesses[-2]-num)>abs(guesses[-1]-num):
				print('Warmer')
			else:
				print('Colder')
		else:
			if abs(guesses[-1]-num)<=10:
				print('Warm')
			else:
				print('Cold')
