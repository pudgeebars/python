#!/bin/bash/python3

import random

print('Guessing Game Rules:\nA random number from 1 to 100 will be generated each round, try to guess that number.')

num =random.randint(1,100)
guess = 0
diff2 = 0
round = 0

while guess!= num:
	guess = int(input('Guess the number:\n'))
	if guess<1 or guess>100:
		print('Out of bounds')
		continue
	diff = guess-num
	if round==0:
		if abs(diff)<10:
			print('warm')
		else:
			print('cold')
	else:
		if abs(diff2) > abs(diff):
			print('warmer')
		else:
			print('colder')
	round+=1            
	diff2=diff
if round==0:
	print(f'Amazing you got it in 1 try, the number is {num}')
print(f'You guessed it in {round} tries, the number is {num}')