# Anthony Tesoriero, Joseph Salemo, Joshua Lunsk, October 2019, Concurrency

# Idea Notes
# Size = n (3 for example); CurrentPosition = pos
# North = -n; South = +n; East = +1; West = -1
# --------------------------------------------------------------------------------- #

import random

# Size of grid (n x n)
# n = input("What is the size of your grid? (n x n) ")
n = 3
# agent1 position is NW corner
agent1 = ["Agent 1", 1]
# agent2 position is SE corner
agent2 = ["Agent 2", n**2]
# Number of gems found out of 4
foundGems = 0


# Gets 4 unique random nums
rands = []
for i in range(8):
	rand = random.randint(1,(n**2)+1)
	if rand not in rands: 
		rands.append(rand)

# gems [name, position]
emerald = ["an emerald", rands[0]]
crown = ["a crown", rands[1]]
coin = ["a coin", rands[2]]
book = ["a rare book", rands[3]]

# List of gems
gems = [emerald, crown, coin, book]

# Checks if direction attempt is valid
# dir: 1 = north, 2 = east, 3 = south, 4 = west
def checkDir(self, agent, dir):
	# North
	if dir is 1 and agent[1] - n < 1:
		return False

	# East
	if dir is 2 and agent[1] % n is 0:
		return False

	# South
	if dir is 3 and agent[1] + n > n**2:
		return False

	# West
	if dir is 4 and (agent[1] - 1) % n is 0:
		return False
	
	# No failures
	return True

# print(checkDir(agent1, 1), checkDir(agent1, 2), checkDir(agent1, 3), checkDir(agent1, 4))

def findGem(gem, agent):
	global foundGems
	foundGems	+= 1
	print(agent[0], "found", gem[0], "in room", gem[1])
	print(4-foundGems, "gems left.")
	gem[1] = -1
	
# findGem(emerald, agent1)

# Find if agent position equals gems
def gemCheck(agent):
	for i in gems:
		if agent[1] is i[1]:
			findGem(i, agent)
			
gemCheck(agent1)
