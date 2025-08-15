# PythonPlay

This is a simple console-based Tic-Tac-Toe game implemented in Python. The game allows two players to take turns choosing positions on a 3x3 grid, using 'X' and 'O' as their markers. The program validates user input, checks for winning conditions after each move, and announces the winner or a draw when the game ends.
 
## How to Run

1. Make sure you have Python installed on your system.
2. Open a terminal in this project directory.
3. Run the following command:

	 ```bash
	 python TicTacToe.py
	 ```

## Game Instructions

- At the start, you will be prompted to choose your marker: `X` or `O`.
- Players take turns entering a position (1-9) to place their marker on the board:
	- The board positions are numbered as follows:

		1 | 2 | 3
		---------
		4 | 5 | 6
		---------
		7 | 8 | 9

- Enter the number corresponding to your desired position when prompted.
- The game will display the board after each move.
- If a player gets three of their markers in a row (horizontally, vertically, or diagonally), they win.
- If all positions are filled and no player has won, the game ends in a draw.

## Example Output

```
Choice (X/O): X
Enter a your Position (1-9) : 5
 ------ X ----- X -----
	|   |   |  
--|---|---|--
	| X |   |  
--|---|---|--
	|   |   |  
 ------ X ----- X -----
```

Follow the prompts until the game announces a winner or a draw.