"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""


import random as r


def main():
	"""
	This will do flip coin and give you results of streakT or streakH according the number you want.
	"""
	print("Let's flip a coin!")
	num_run = int(input('Number of runs: '))  # The time of streak you want.
	coin1 = r.randrange(0, 2)  # Get first coin is 0 or 1.
	same_side = False
	flip = 0
	results = ''
	while True:
		if flip != num_run:
			coin2 = r.randrange(0, 2)  # Get second coin is 0 or 1
			results += str(coin2)  # Record results.
			if coin1 == coin2:
				if not same_side:
					flip += 1  # Streak one.
					same_side = True  # Change the bool so the loop continue.
			else:
				same_side = False
			coin1 = coin2  # Rename coin1 so the loop continue.
		else:
			break
	answer = ''  # Change 0 and 1 to T and H.
	for coin in results:
		if coin == '0':
			answer += 'T'
		else:
			answer += 'H'
	print(str(answer))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
