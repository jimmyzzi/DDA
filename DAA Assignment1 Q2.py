import asyncio
import platform
import pygame
import time
from typing import List
import sys

# Initialize Pygame and set constants (global variables for visualisation)
def setup():
    global screen, board_size, cell_size, width, height, queens, font
    pygame.init()   #Initialises Pygame library
    board_size = 8  # Default N for visualization (Default board size)
    cell_size = 80  #Size of each squre in pixel
    width = height = board_size * cell_size #Calculates the windows dimesnions
    screen = pygame.display.set_mode((width, height)) #Create a display window
    pygame.display.set_caption("N-Queens Visualization")
    queens = []
    font = pygame.font.SysFont("Arial", 40)
    # Colors
    global WHITE, BLACK, RED
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

# Check if placing a queen at (row, col) is safe
def is_safe(board: List[List[int]], row: int, col: int, n: int) -> bool:
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper-left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper-right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False
    
    return True

# Solve N-Queens using backtracking using a recursive function
def solve_n_queens(board: List[List[int]], row: int, n: int, solutions: List[List[List[int]]]) -> bool:
    global solve_start_time
    if row == n:
        # Store a copy of the board as a solution
        solutions.append([row[:] for row in board])
        return True
    
    found_solution = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = 0  # Backtrack
            found_solution = True
    return found_solution

# Initialize an NxN board (with zeros)
def initialize_board(n: int) -> List[List[int]]:
    return [[0 for _ in range(n)] for _ in range(n)]

# Performance analysis for different N (board sizes)
def analyze_performance(max_n: int = 12):
    global performance_data
    performance_data = []
    print("Performance Analysis:")
    for n in range(4, max_n + 1): #Test board sizes from 4 to max_N
        board = initialize_board(n) #Creates a new board
        solutions = []  #List to store solutions
        start_time = time.time()  #Records start time
        solve_n_queens(board, 0, n, solutions)
        end_time = time.time()  #Records end time
        time_taken = end_time - start_time  #Calculate time taken
        performance_data.append((n, len(solutions), time_taken)) #Stores results
        print(f"N={n}: {len(solutions)} solutions, Time={time_taken:.4f} seconds")

# Draw the chessboard and queens
def draw_board():
    screen.fill(WHITE)
    for row in range(board_size):
        for col in range(board_size):
            color = WHITE if (row + col) % 2 == 0 else BLACK #Alternate colours for chessboard pattern
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))
            if (row, col) in queens:
                # Draw queen symbol
                text = font.render("♕", True, RED)
                text_rect = text.get_rect(center=(col * cell_size + cell_size // 2, row * cell_size + cell_size // 2))
                screen.blit(text, text_rect)
    pygame.display.flip()

# Update loop for visualization
async def update_loop():
    global queens, current_solution, solution_index, solutions
    for event in pygame.event.get(): #Handles events
        if event.type == pygame.QUIT: #Closse the window
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and solutions:  #Spacebar to cycle solutions
                # Move to next solution
                solution_index = (solution_index + 1) % len(solutions)
                current_solution = solutions[solution_index]
                queens = [(i, j) for i in range(board_size) for j in range(board_size) if current_solution[i][j] == 1]
    
    draw_board()  #Redraws the board
    await asyncio.sleep(0.1)  #Controls the frame rate

# Main function
async def main():
    global queens, current_solution, solution_index, solutions, board_size
    setup()
    
    # Solve for default board size
    board = initialize_board(board_size)
    solutions = []
    solve_n_queens(board, 0, board_size, solutions)
    solution_index = 0
    if solutions:
        current_solution = solutions[0]
        queens = [(i, j) for i in range(board_size) for j in range(board_size) if current_solution[i][j] == 1]
    
    # Run performance analysis
    analyze_performance()
    
    # Main loop for visualisation
    while True:
        await update_loop()

# Pyodide-compatible execution
if platform.system() == "Emscripten":
    asyncio.ensure_future(main())  #Run in browser
else:
    if __name__ == "__main__":
        asyncio.run(main())  #Run locally
