Board = [[' ', ' | ', ' ',' | ', ' '],
         ['-', ' | ', '-',' | ', '-'],
         [' ', ' | ', ' ',' | ', ' '],
         ['-', ' | ', '-',' | ', '-'],
         [' ', ' | ', ' ',' | ', ' ']]

BoardPos = {1 : (0, 0), 2 : (0, 2), 3 : (0, 4),
            4 : (2, 0), 5 : (2, 2), 6 : (2, 4),
            7 : (4, 0), 8 : (4, 2), 9 : (4, 4)}

## Check for Empty Positions
def empty_positions():
    for i in range(len(Board)):
        for j in range(len(Board[0])):
            if i%2 == 0 and j%2 == 0:
                if Board[i][j] == ' ':
                    return True
    return False 

## Print the Board
def print_board():
    for i in range(len(Board)):
        for j in range(len(Board[i])):
            print(Board[i][j],end =' ')
        print()

## Validate User Input position
def validate_input():
    waiting_for_input = True
    while waiting_for_input:
        try:
            ## Get the User Position Input
            user_input = int(input('Enter a your Position (1-9) : '))
        except:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        else:
            (x,y)  = BoardPos[user_input]
            waiting_for_input = not(Board[x][y] == ' ')
            ## If input is valid, exit loop
            if waiting_for_input:
                print("Position already taken by Player {}. Please choose another.".format(Board[x][y]))
    return user_input

## Change User Input for each iteration
def change_user_input(user_input):
    if user_input == 'X':
        return 'O'
    return 'X'

## Verify User Choice
def verify_user_input():
    waiting_for_input = True
    while waiting_for_input:
        try:
            ## Get the User Choice of Input (X/O)
            user_input = input('Choice (X/O): ')

            ##Throw error if input is not X or O
            if user_input not in ['X', 'O']:
                raise TypeError
        except TypeError:
            print('Please enter a valid choice (X/O).')
            continue
        else:
            ## If input is valid, exit loop
            waiting_for_input = False
    return user_input

def validate_winner():
    ## Horizontal check
    for i in range(0,len(Board), 2):
        if Board[i][0] == Board[i][2] == Board[i][4] and Board[i][0] != ' ':
            print()
            print("Player {} wins!".format(Board[i][0]))
            print()
            return False
        
    ## Vertical check
    for i in range(0, len(Board[0]), 2):
        if Board[0][i] == Board[2][i] == Board[4][i] and Board[0][i] != ' ':
            print()
            print("Player {} wins!".format(Board[0][i]))
            print()
            return False
        
    ## Left Diagonal Check
    if Board[0][0] == Board[2][2] == Board[4][4] and Board[0][0] != ' ':
        print()
        print("Player {} wins!".format(Board[0][0]))
        print()
        return False

    ## Right Diagonal Check
    if Board[0][4] == Board[2][2] == Board[4][0] and Board[0][4] != ' ':
        print()
        print("Player {} wins!".format(Board[0][4]))
        print()
        return False
    
    return True

## Get the User Choice of Input (X/O)
user_input = verify_user_input()

## Game Loop
while empty_positions() and validate_winner():
    user_position = validate_input()
    (x,y) = BoardPos[user_position]
    Board[x][y] = user_input

    print(' ------ X ----- X -----')
    print_board()
    print(' ------ X ----- X -----')
    
    user_input = change_user_input(user_input)

if not empty_positions():
    print()
    print("It's a draw!")
    print()