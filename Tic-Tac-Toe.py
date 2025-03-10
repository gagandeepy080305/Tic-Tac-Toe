winner=None
check_gamerunning=True
currentPlayer='O'
board=['-','-','-',
       '-','-','-',
       '-','-','-']
#Printing the updated board after every turn
def updateBoard(board):
  print(board[0], " | ",board[1], " | ", board[2])
  print(board[3], " | ",board[4], " | ", board[5])
  print(board[6], " | ",board[7], " | ", board[8])
#Accept input
def play(board):
  if winner == None and check_gamerunning == True: #stops the game if winner is declared.
    turns=int(input("Enter a number 1-9 : "))
    if turns>=1 and turns<=9 and board[turns-1] == '-':#To check if there is empty space to print  either 'X' or 'O'
        board[turns-1]=currentPlayer
    else:
        print("No space available")
#Check Winner
def check_rows(board):
  global winner#To change the value of winner globally in all the functions
  if board[0] == board[1] == board[2] and board[0] != '-':
    winner=board[0]
  elif board[3] == board[4] == board[5] and board[3] != '-':
    winner=board[3]
  elif board[6] == board[7] == board[8] and board[6] != '-':
    winner=board[6]
  return True
def check_columns(board):
  global winner
  if board[0] == board[3] == board[6] and board[0] != '-':
    winner=board[0]
  elif board[1] == board[4] == board[7] and board[1] != '-':
    winner=board[1]
  elif board[2] == board[5] == board[8] and board[2] != '-':
    winner=board[2]
  return True
def check_diagonal(board):
  global winner
  if board[0] == board[4] == board[8] and board[0] != '-':
    winner=board[0]
  elif board[2] == board[4] == board[6] and board[2] != '-':
    winner=board[2]
  return True
def checkWin():
  global check_gamerunning
  if check_gamerunning == True:
    if (check_rows(board) or check_columns(board) or check_diagonal(board)) and winner != None:
      print(f"{winner} is the winner")
      check_gamerunning=False
    #while winner != None:
      #break 
#check for Tie
def check_Tie(board):
  global check_gamerunning
  count=0
  for i in range (0,len(board)):
    if board[i] == '-':
      count+=1
  if count == 0:
    print("Draw!")
    check_gamerunning=False
#Switch players
def switchPlayer():
  global currentPlayer
  if currentPlayer == 'X':
    currentPlayer='O'
  else:
    currentPlayer='X'
while check_gamerunning:
  updateBoard(board)
  check_rows(board)
  check_columns(board)
  check_diagonal(board)
  check_Tie(board)
  checkWin()
  switchPlayer()
  play(board)
  