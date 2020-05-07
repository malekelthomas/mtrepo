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
		self.board[x][y] = "|"+xoro+"|"
    
	def gameNotFinished(self):
		if '|_|' in self.board[0]:
			return True
		else:
			return False

class ticTacToePlayer():
	def __init__(self, name, xoro):
		self.name = name
		self.score = 0
		self.xoro = xoro

	def addToScore(self):
		self.score+=1

class ticTacToeGame():
	def __init__(self):
		self.board = ticTacToeBoard()
		self.players = []
	
	def inputToMove(self, move):
		x = move
		return move.split(",")

	def startGame(self):
		player1 = input("Player 1 name?: ")
		self.players.append(ticTacToePlayer(player1, "X"))

		player2 = input("Player 2 name?: ")
		self.players.append(ticTacToePlayer(player2, "O"))

	

		while self.board.gameNotFinished():
			print("Players:", self.players[0].name, self.players[1].name,)
			print("Score: ", self.players[0].score, self.players[1].score)
			self.board.drawBoard()
			player1move = self.inputToMove(input(self.players[0].name+" , where do you want to place X?"))
			self.board.addToBoard("X", int(player1move[0]), int(player1move[1]))
			print("..placing")
			self.board.drawBoard()
			player2move = self.inputToMove(input(self.players[1].name+" , where do you want to place O?"))
			self.board.addToBoard("O", int(player2move[0]), int(player2move[1]))
			print("..placing")
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


