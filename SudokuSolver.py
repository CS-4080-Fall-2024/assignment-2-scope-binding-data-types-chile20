def solve_sudoku(board):
    def is_valid(board, row, col, num):
        # Check if num already exists whichin row and column
        for i in range(0, 9):
            if board[row][i] == num or board[i][col] == num:
                return False

        # Calculate the starting point for the 3x3 subgrid the cell belongs to
        start_row = 3 * (row // 3)
        start_col = 3 * (col // 3)

        # Check if the number exists within the 3x3 subgrids
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False

        # If no conflicts, the number placement is valid
        return True

    # Backtracking algorithm to fill the board
    def backtrack(board):
        # Iterate over each cell in the 9x9 grid
        for row in range(9):
            for col in range(9):
                # Find an empty cell
                if board[row][col] == ".":
                    # Try placing numbers 1 through 9 in the cell
                    for num in map(str, range(1, 10)):
                        if (is_valid(board, row, col, num)):
                            board[row][col] = num
                            # Recursively try to complete the board with this number
                            if backtrack(board):
                                return True
                            # If it leads to a dead end, backtrack by resetting the cell
                            board[row][col] = "."

                    # If no valid numbers fit, return False to trigger backtracking
                    return False
        # If all cells are filled correctly, return True
        return True

    backtrack(board)


# Function to print the Sudoku board
def print_board(board):
    for row in board:
        print(" ".join(row))


# Sample board for testing
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print("Original board:")
print_board(board)
solve_sudoku(board)
print("\nSolved board:")
print_board(board)