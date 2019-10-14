# Anthony Tesoriero, Joseph Salemo, Joshua Lunsk, October 2019, Concurrency

# Idea Notes
# Size = n (3 for example); CurrentPosition = pos
# North = -n; South = +n; East = +1; West = -1
# --------------------------------------------------------------------------------- #

import random


# ---------- Initialization ---------- #
class Concurrency:

	def __init__(self):

		# Size of grid (n x n)
		# self.n = int(input("What is the size of your grid? (n x n) "))
		self.n = 3
		# self.version = int(input("Input '1' for starting in opposite corners, '2' for random movements: "))
		self.version = 1

		# Initialize agents [Name, space, current direction]
		self.agent1 = ["Agent 1", 1, 3]
		self.agent2 = ["Agent 2", self.n**2, 1]
		self.foundGems = 0

		# Gets 4 unique random nums
		rands = []
		for i in range(8):
			rand = random.randint(1, self.n ** 2)
			if rand not in rands:
				rands.append(rand)

		# List of gems [name, position]
		self.gems = [["an emerald", rands[0]], ["a crown", rands[1]], ["a coin", rands[2]], ["a rare book", rands[3]]]
		
		self.spiralRun()

	# ---------- Functions ---------- #

	def setType(self):
		if self.version is 2:
			# agent1 and agent2 position random
			self.agent1[1] = random.randint(1, 9)
			self.agent2[1] = random.randint(1, 9)

	# Checks if direction attempt is valid
	# dir: 1 = north, 2 = east, 3 = south, 4 = west
	def checkDir(self, agent, dir):
		# North
		if dir is 1 and agent[1] - self.n < 1:
			return False
		# East
		if dir is 2 and agent[1] % self.n is 0:
			return False
		# South
		if dir is 3 and agent[1] + self.n > self.n ** 2:
			return False
		# West
		if dir is 4 and (agent[1] - 1) % self.n is 0:
			return False
		# No failures
		return True

	# Moves agent
	# dir: 1 = north, 2 = east, 3 = south, 4 = west
	def move(self, agent, dir):
		if dir is 1 and self.checkDir(agent, dir):
			agent[1] -= self.n
		if dir is 2 and self.checkDir(agent, dir):
			agent[1] += 1
		if dir is 3 and self.checkDir(agent, dir):
			agent[1] += self.n
		if dir is 4 and self.checkDir(agent, dir):
			agent[1] -= 1

	# Random movement
	def randomMoveDir(self):
		return random.randint(1, 4)

	# Finds gem with agent
	def findGem(self, gem, agent):
		self.foundGems += 1
		print(agent[0], "found", gem[0], "in room", gem[1])
		print(4 - self.foundGems, "gems left.")
		gem[1] = -1

	# Find if agent position equals gems
	def gemCheck(self, agent):
		for gem in self.gems:
			if agent[1] is gem[1]:
				self.findGem(gem, agent)
	
	# Run
	def spiralRun(self):
		self.setType()
		
		"""
		while self.foundGems != 4:
			while self.checkDir(self.agent1, 3):
				self.move(self.agent1, 3)
				self.gemCheck(self.agent1)
				self.move(self.agent2, 1)
				self.gemCheck(self.agent2)
				print("loop1")
			while self.checkDir(self.agent1, 2):
				self.move(self.agent1, 2)
				self.gemCheck(self.agent1)
				self.move(self.agent2, 4)
				self.gemCheck(self.agent2)
				print("loop2")
			while self.checkDir(self.agent1, 1):
				self.move(self.agent1, 1)
				self.gemCheck(self.agent1)
				self.move(self.agent2, 3)
				self.gemCheck(self.agent2)
				print("loop3")
			while self.checkDir(self.agent1, 4):
				self.move(self.agent1, 4)
				self.gemCheck(self.agent1)
				self.move(self.agent2, 2)
				self.gemCheck(self.agent2)
				print("loop4")
			"""
			
		print(self.gems)
		print("All gems found!")
				

# ---------- Driver ---------- #

# Run Concurrency
game = Concurrency()
