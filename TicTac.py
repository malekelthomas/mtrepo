class ticTacToeBoard():
	def __init__(self):
		self.board = [["|_|", "|_|", "|_|"],["|_|", "|_|", "|_|"],["|_|", "|_|", "|_|"]]
	
	def drawBoard(self):	
		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				print(self.board[i][j], end= " ")
			if(i == len(self.board)-1):
				print("\n")
				break
			print("\n-----------")
	
	def addToBoard(self, xoro, x, y):
		self.board[x][y] = xoro
    
	def gameNotFinished(self):
		if '|_|' in self.board:
			return True
		else:
			return False

class ticTacToePlayer():
	def __init__(self, name):
		self.name = name
		self.score = 0
	
	def addToScore(self):
		self.score+=1

class ticTacToeGame():
	def __init__(self):
		self.board = ticTacToeBoard()
		self.players = []
		self.scoreBoard = []
	
	def startGame(self):
		x = input("Player 1 name?: ")
		self.players.append(ticTacToePlayer(x))

		y = input("Player 2 name?: ")
		self.players.append(ticTacToePlayer(y))
		print(self.board.gameNotFinished())
		while self.board.gameNotFinished():
			self.board.drawBoard()







def main():
	x = ticTacToeGame()
	x.startGame()
if __name__ == '__main__':
	main()


# x = input("Place x where?")

# y = int(x.split(",")[0])

# z = int(x.split(",")[1])

# print(y,z)


# l[y][z] = "|X|"



# for i in range(len(l)):
# 	for j in range(len(l[i])):
# 		print(l[i][j], end= " ")
# 	print("\n-----------")


