
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

score = {'Player 1': 0, 'Player 2': 0}

def printBoard(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("\n")

def spaceIsFree(position):
    if board[position] == ' ':
        return True
    return False

def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if checkDraw():
            print("Draw!")
            exit()
        if checkWin():
            if letter == 'X':
                print("Player 2 wins!")
                score['Player 2'] += 1
            else:
                print("Player 1 wins!")
                score['Player 1'] += 1
            printScoreboard()
            resetBoard()
        return
    else:
        print("Invalid position")
        position = int(input("Please enter a new position: "))
        insertLetter(letter, position)
        return

def checkWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

def playerMove(player):
    position = int(input(f"Player {player}, enter a position: "))
    insertLetter('X', position)
    return

def resetBoard():
    for key in board.keys():
        board[key] = ' '

def printScoreboard():
    print("Scoreboard:")
    print("Player 1:", score['Player 1'])
    print("Player 2:", score['Player 2'])
    print()

while True:
    printBoard(board)
    playerMove(1)
    printBoard(board)
    if checkWin():
        print("Player 1 wins!")
        score['Player 1'] += 1
        printScoreboard()
        resetBoard()
        continue
    if checkDraw():
        print("Draw!")
        resetBoard()
        continue
    playerMove(2)
    if checkWin():
        print("Player 2 wins!")
        score['Player 2'] += 1
        printScoreboard()
        resetBoard()
        continue
    if checkDraw():
        print("Draw!")
        resetBoard()
        continue



# a = [4+8j,True]
# # print(a[1][1])
# True_str=str(a[1])
# first_letter = True_str[0]
# print(first_letter)

# a = [4 + 8j, True]
# true_str = str(a[1])
# first_letter = true_str[0]
# print(first_letter)



# a=[1,2,3,4,5]
# print((a))

# n=int(input(":"))
# if n % 2 != 0:
#     print("Weird")
# else:
#     if n >= 2 and n <= 5:
#         print("Not Weird")
#     elif n >= 6 and n <= 20:
#         print("Weird")
#     elif n > 20:
#         print("Not Weird")

# for i in range(10, 15,1):
#   print( i, end=' ')

# sampleList = ["Jon", "Kelly", "Jessa"]
# sampleList.append([2]("Scott"))
# print(sampleList)

var= "James Bond"
print(var[2:-3:3])







