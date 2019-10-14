# Anthony Tesoriero, Joseph Salemo, Joshua Lunsk, October 2019, Concurrency

# Idea Notes
# Size = n (3 for example); CurrentPosition = pos
# North = -n; South = +n; East = +1; West = -1
# --------------------------------------------------------------------------------- #

import random

# n = input("What is the size of your grid? (n x n) ")
n = 3
# agent1 pos = NW corner
agent1 = 1
# agent2 pos = SE corner
agent2 = n**2


# Gets 4 unique random nums
rands = []
for i in range(8):
	rand = random.randint(1,(n**2)+1)
	if rand not in rands: 
		rands.append(rand)

emrald = rands[0]
crown = rands[1]
coin = rands[2]
book = rands[3]


# Checks if direction attempt is valid
# dir: 1 = north, 2 = east, 3 = south, 4 = west
def checkDir(agent, dir):
	# North
	if dir is 1 and agent - n < 1:
		return False

	# East
	if dir is 2 and agent % n is 0:
		return False

	# South
	if dir is 3 and agent + n > n**2:
		return False

	# West
	if dir is 4 and (agent - 1) % n is 0:
		return False
	
	# No failures
	return True

# print(checkDir(agent1, 1), checkDir(agent1, 2), checkDir(agent1, 3), checkDir(agent1, 4))
