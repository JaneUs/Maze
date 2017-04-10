class Maze:
	
	def __init__(self, map, hero, guard, gameover, heromoved):
		self.map = map
		self.hero = hero
		self.guard = guard
		self.gameover = gameover
		self.heromoved= heromoved

	hero = (1, 1)
	guard = (1, 8)
	map = [['X', 'X', 'X','X', 'X', 'X', 'X', 'X', 'X','X'], 
	      ['X', ' ', ' ',' ', 'I', ' ', 'X', ' ', ' ','X'], 
	      ['X', 'X', 'X',' ', 'X', 'X', 'X', ' ', ' ','X'], 
	      ['X', ' ', 'I',' ', 'I', ' ', 'X', ' ', ' ','X'], 
	      ['X', 'X', 'X',' ', 'X', 'X', 'X', ' ', ' ','X'], 
	      ['I', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ','X'], 
	      ['I', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ','X'], 
	      ['X', 'X', 'X',' ', 'X', 'X', 'X', 'X', ' ','X'], 
	      ['X', ' ', 'I',' ', 'I', ' ', 'X', 'k', ' ','X'], 
	      ['X', 'X', 'X','X', 'X', 'X', 'X', 'X', 'X','X']]
	gameover = False
	heromoved = False

#	def gameover():
#		if self.gameover == True:
#			print('Game over!')
#			break

	def movehero():
		if move == 'w' or move == 'W':
			if self.hero[0] > 0 and (self.map[self.hero[0]-1][self.hero[1]] == ' ' or self.map[self.hero[0]-1][self.hero[1]] == 'k' or self.map[self.hero[0]-1][self.hero[1]] == 'S'):
				self.hero[0] -= 1
				self.heromoved = True
			else:
				print('Impossible to move up')

		elif move == 's' or move == 'S':
			if self.hero[0] < 9 and (self.map[self.hero[0]+1][self.hero[1]] == ' ' or self.map[self.hero[0]+1][self.hero[1]] == 'k' or self.map[self.hero[0]+1][self.hero[1]] == 'S'):
				self.hero[0] += 1
				self.heromoved = True
			else:
				print('Impossible to move down')			

		elif move == 'a' or move == 'A':
			if self.hero[1] > 0 and (self.map[self.hero[0]][self.hero[1]-1] == ' ' or self.map[self.hero[0]][self.hero[1]-1] == 'k' or self.map[self.hero[0]][self.hero[1]-1] == 'S'):
				self.hero[1] -= 1
				self.heromoved = True
			else:
				print('Impossible to move left')

		elif move == 'd' or move == 'D':
			if self.hero[1] < 9 and (self.map[self.hero[0]][self.hero[1]+1] == ' ' or self.map[self.hero[0]][self.hero[1]+1] == 'k' or self.map[self.hero[0]][self.hero[1]+1] == 'S'):
				self.hero[1] += 1
				self.heromoved = True
			else:
				print('Impossible to move right')	
		else:
			return

	def moveguard():
		if self.guard[0] == 1 and self.guard[1] == 8:
			self.guard[1] = 7
		elif self.guard[1] == 7 and self.guard[0] < 5:
			self.guard[0] += 1
		elif self.guard[0] == 5 and self.guard[1] < 8 and self.guard[1] > 1:
			self.guard[0] -= 1		
		elif self.guard[0] == 5 and self.guard[1] == 1:
			self.guard[0] += 1
		elif self.guard[0] == 6 and self.guard[1] < 8:
			self.guard[1] += 1
		elif self.guard[1] == 8 and self.guard[0] > 1:
			self.guard[0] -= 1

	def checkhero():
		if self.map[self.hero[0]][self.hero[1]] == 'S':
			print('Congratulations! You quit the maze!')
			self.gameover = True
		elif self.map[self.hero[0]][self.hero[1]] == 'k':
			print('Doors are opened!')
			self.map[5][0] = self.map[6][0] = 'S'
		elif (self.hero[0]==self.guard[0] and (self.hero[1]==self.guard[1] or self.hero[1]+1==self.guard[1]  or self.hero[1]-1==self.guard[1])) or (self.hero[1]==self.guard[1] and (self.hero[0]+1==self.guard[0]  or self.hero[0]-1==self.guard[0])):
			print('You are captured! Game over!')
			self.gameover = True

	def printmaze():
		for i in range(0, 9, 1):
			for h in range(0, 10, 1):
				if self.guard[0] == i and self.guard[1] == h:
					print('G ')
				elif self.hero[0] == i and self.hero[1] == h:
					print('H ')
				else:
					print(self.map[i][h] + ' ')



	move = 'n'
	while move != 'p' and Maze.gameover() != True:
		move = input('Use only "wasd" to move and "p" to quit: ')			
		if move not in ['w', 'a', 's', 'd', 'W', 'A', 'S', 'D', 'p', 'P']:
			print('Use only "wasd" to move or "p" to quit.')
		elif move in ['w', 'a', 's', 'd', 'W', 'A', 'S', 'D']:
			Maze.movehero()
			if Maze.heromoved:
				Maze.guard()
				Maze.checkhero()
				Maze.map()
				Maze.heromoved = False
		elif move == 'p' or move == 'P':
			print('Game over. Bye.')
			break