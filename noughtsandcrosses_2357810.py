import random   #Importing Random Module
import os.path
import json

random.seed()

def draw_board(board):
    ''' This function will draw the 2-dimensional Noughts and Crosses Board. '''
    print(
' +---+---+---+\n',
'|',board[0][0] ,'|', board[0][1], '|', board[0][2], '|\n'
' +---+---+---+\n',
'|',board[1][0], '|', board[1][1], '|', board[1][2], '|\n',
'+---+---+---+\n',
'|',board[2][0], '|', board[2][1], '|', board[2][2], '|\n',
'+---+---+---+\n',)
pass

def welcome(board):
    ''' At first, This function will displays the welocme message as: Welcome To The Noughts and Crosses Game.
    and also displays The layout of the board is shown below.
      After that, It called the function draw_board(board) for displaying the board. '''
    print("Welcome To The Unbeatable Noughts and Crosses Game")
    print("The layout of the board is shown below.")
    draw_board(board)

def initialise_board(board):
    '''This function will gives a single space for all the elements of the board'''
    for i in range(3):
        for j in range(3):
            board[i][j] = " "
    return board

def get_player_move(board):
    '''This function will take the user input number that represent the cell to put the X in it.
    And Return The Row and Column'''
    Right_step = False
    while not Right_step:
        try:
            print('                    1 2 3')
            print('                    4 5 6')
            choose_square= int(input("Choose your square: 7 8 9 : "))    #give option to choose the number according to the cell's number
            choose_square = choose_square-1   # changing the user inputs into the zero-based indexing 
            rows = choose_square//3
            columns = (choose_square%3)
            if choose_square < 0 or choose_square > 9:
                print("Invalid input, please try again.")
            elif board[rows][columns] != ' ':
                print("This cell was already Occupied, Try Again!.")   # it gives alert message as cell was already occupied 
            else:
                Right_step = True
        except ValueError:
            print("Invalid!, Try Again.")
    return rows, columns                   #return row and columns

def choose_computer_move(board):
    '''This function will take the computer choice to put a Nought in.
    And Return the Row and Column'''
    unoccupied_cells = []           #An Empty cell was created for storing scores
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                unoccupied_cells.append((i, j))  #Apppends the values in the Unoccupied_cells

    if not unoccupied_cells:
        return None

    return random.choice(unoccupied_cells)

def check_for_win(board, mark):
    '''This function check either the computer has won or the player has won.
    And Return True if player has won, otherwise return False'''
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == mark:
            return True
        if board[0][i] == board[1][i] == board[2][i] == mark:
            return True
    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True
    return False

def check_for_draw(board):
    '''This function will check either all cells are occupied or not.
    Return True if all cells are occupied, otherwise Return False'''
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True
        
def play_game(board):
    '''This function is responsible for playing the game
    At First, it call the function initialise_board(board) to set the board cells to all single spaces
    Then, it call the function draw_board(board) to draw the board
    Then,  using the while loop to get the player move'''

    board = initialise_board(board)  # Initialising the board
    draw_board(board)                # Draw the board

    # Game loop
    while True: 
        # getting the Player's move
        rows, columns = get_player_move(board)  
        board[rows][columns] = "X"           #Updating the board
        draw_board(board)               #Draw the board
        if check_for_win(board, "X"):   #checking either the player won or not
            return 1                    #if player has won, return 1
        elif check_for_draw(board):     #checking either draw or not
            return 0                    # if draw, return 0
        
        #Computer's Move
        rows, columns = choose_computer_move(board)  
        board[rows][columns] = "O"           #Updating the board
        draw_board(board)               #Draw the board
        if check_for_win(board, "O"):   #checking either the computer won or not
            return -1                   #if computer has won, return -1
        elif check_for_draw(board):     #checking either draw or not
            return 0                    # if draw, return 0
        

def menu():
    '''This function give the option to the user to chose:
    1- Play the game
    2 - Save score in file
    3 - Load and display the scores from the file
    q - End the program
    '''
    while True:
        print("Choose one of the following options:")
        print("1 - Play the game")
        print("2 - Save score in file 'leaderboard_2357810.txt'")
        print("3 - Load and display the scores from the 'leaderboard_2357810.txt'")
        print("q - End the program")
        choice = input("Enter your choice: ")
        if choice in ['1', '2', '3', 'q']:     #using the membership concept to check the user input is in the list [1,2,3,q]
            return choice                      #if the item is in the list, Return the choice
        else:
            print("Invalid choice!, Try Again.")  #if the items is not in the list, it gives the invalid choice as a message

def load_scores():
    '''This function will load the scores from the leaderboard_2357810.txt file
    and returns the scores in dictionary form as like as player_name: scores
    return the leaders in dictionary form'''

    with open("leaderboard_2357810.txt", "r") as f:
        leaders = json.load(f)                      #it loads the scores from the leaderboard_2357810.txt file
    return leaders                                  #returns the leaders value

def save_score(score):
    '''This function will ask the name of the player at first.
     Then, opens the leaderboard_2357810.txt file in read mode.
      Using the Exception handling concept, try to load the score on the file.
      if the file is not exists then, it automatically creates the new dictionary.
      Then,  json.load(f) will loads the scores from the leaderboard_2357810.txt file.
       whereas jason.dump() will save the updated score of the players in the leaderboard_2357810.txt file '''
    
    player_name = input("Enter your Name: ")
    try:
        with open('leaderboard_2357810.txt', 'r') as f:
            leaders = json.load(f)                   #it loads the scores from the leaderboard_2357810.txt file
    except FileNotFoundError:
        leaders = {}
    leaders[player_name] = score
    with open('leaderboard_2357810.txt', 'w') as f:
        json.dump(leaders, f)                         #save the updated scores of the players
        

def display_leaderboard(leaders):
    '''This function will displays the leaderboard to the user in the form of dictionary'''
    print("leaderboard:")
    for player_name, score in leaders.items():
        print(f"{player_name}:{score}")
    pass

