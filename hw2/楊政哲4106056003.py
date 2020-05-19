broad = [[3, 4, 0], [4, 3, 0], [3, 3, 1], [4, 4, 1]]
steps = [[5, 4], [5, 5]]


board = []
B = "B"
W = "W"

def GetBoard():
	for i in range(0, 8):
		new = []
		for j in range(0, 8):
			new.append(-1)
		board.append(new)
	
	for x in range(8):
		for y in range(8):
			board[x][y] = -1
			
	for i in range( len(broad)):
		x = broad[i][1]
		y = broad[i][0]
		if( broad[i][2] == 0):
			board[x][y] = 0
		elif( broad[i][2] == 1):
			board[x][y] = 1

def GetBroad():
	broad = []
	for x in range(8):
		for y in range(8):
			if board[x][y] != -1:
				broad.append( [ y, x, board[x][y]])
	return broad

def getScore():
	# 取得目前分數
	BScore = 0
	WScore = 0
	for i in range( len(broad)):
		if broad[i][2] == 0:
			BScore += 1
		if broad[i][2] == 1:
			WScore += 1
	return {"B":BScore, "W":WScore}

def isOnBoard(x, y):
	# 確認本位置仍在棋盤上
    return x >= 0 and x <= 7 and y >= 0 and y <=7

def isValidMove(tile, XStart, YStart):
	# 確認本位置是否能夠下子
	# 如果能夠下子，回傳本次下子需要翻面對方子的陣列
	if ( board[XStart][YStart] != -1) or ( not isOnBoard(XStart, YStart)):
		return False
	# 暫時下子
	board[XStart][YStart] = tile
	# 確定顏色
	if tile == 1:
		otherTile = 0
	else:
		otherTile = 1
	
	tilesToFlip = []
	for XDir, YDir in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
		x, y = XStart, YStart
		x += XDir
		y += YDir
		if isOnBoard(x, y) and board[x][y] == otherTile:
			# 此方向仍在棋盤上而且有對方子
			x += XDir
			y += YDir
			if not isOnBoard(x, y):
				continue
			while board[x][y] == otherTile: # 延伸到可以下子
				x += XDir
				y += YDir
				if not isOnBoard(x, y):
					break
			if not isOnBoard(x, y): # 避免延伸到棋盤外
				continue

			if board[x][y] == tile: # 此方向尾端是我方子，紀錄沿路上的對方子（需要翻面）
				while True:
					x -= XDir
					y -= YDir
					if x == XStart and y == YStart:
						break
					tilesToFlip.append([x, y])

	board[XStart][YStart] = -1 # 測試完畢，恢復棋盤
	if len(tilesToFlip) == 0: # 無對方子需要翻面 = 非有效下子位置
		return False
		
	return tilesToFlip

def makeMove(tile, XStart, YStart):
	# 下子測試
	tilesToFlip = isValidMove(tile, XStart, YStart)
	
	if tilesToFlip == False: # 如果非有效下子，取消下子
		print( "error move")
		return False
	
	board[XStart][YStart] = tile
	for x, y in tilesToFlip:
		board[x][y] = tile
	return True

print("1.")
scores = getScore()
if scores[B] > scores[W]:
	print("black")
elif scores[B] < scores[W]:
	print("white")
else:
	print("tie")

print("2.")
GetBoard()
validMoves = 0
for x in range(8):
	for y in range(8):
		if isValidMove( 0, x, y) != False:	
			validMoves += 1
print(validMoves)

print("3.")
NowTile = 0
for y, x in steps:
	makeMove( NowTile, x, y)
	if NowTile == 0:
		NowTile = 1
	else:
		NowTile = 0
print( GetBroad())