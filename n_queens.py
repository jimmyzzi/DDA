def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 1:
                return False
        
        # Check upper-left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1
        
        # Check upper-right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1
        
        return True
    
    def solve(board, row):
        if row == n:
            # Found a solution, store it
            solution = []
            for i in range(n):
                row_str = ""
                for j in range(n):
                    row_str += "Q" if board[i][j] == 1 else "."
                solution.append(row_str)
            solutions.append(solution)
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                solve(board, row + 1)
                board[row][col] = 0
    
    # Initialize empty board
    board = [[0] * n for _ in range(n)]
    solutions = []
    
    # Start solving from first row
    solve(board, 0)
    return solutions

# Example usage
if __name__ == "__main__":
    n = 4
    solutions = solve_n_queens(n)
    
    print(f"Number of solutions for {n}-Queens: {len(solutions)}")
    for i, solution in enumerate(solutions, 1):
        print(f"\nSolution {i}:")
        for row in solution:
            print(row)