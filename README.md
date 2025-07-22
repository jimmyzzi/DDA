## ***QUESTION 1***

### ***PREREQUISITE:***

-> Ensure you have Python 3.x installed on your system.

-> No external libraries are required as the code uses standard Python libraries (heapq, time, random, collections).

### ***SETUP:***

-> Save the code above in a file named mst_algorithms.py.

-> Open a terminal or command prompt in the directory containing mst_algorithms.py.

***Running the Program:***

-> Execute the script using the command:
     python DAA Assignment1 Q1.py

***The program will:***

-> Run two example test cases with small graphs (4 and 5 vertices) and print the MST edges and total weights for both Prim's and Kruskal's algorithms.

-> Perform a performance comparison on randomly generated graphs with 10, 50, 100, and 500 vertices, using an edge density of 0.3 and averaging over 5 trials.

### ***OUTPUT:***

-> The output will include:

-> Results for the example graphs, showing the MST edges (as tuples of (u, v, weight)) and total weight.

-> A performance table comparing the average execution time and MST weight for Prim's and Kruskal's algorithms across different graph sizes. 

***Example output format:***

Example 1: Small graph with 4 vertices

   _Prim's MST: ([(0, 3, 5), (3, 2, 4), (0, 1, 10)], 19)_

   _Kruskal's MST: ([(2, 3, 4), (0, 3, 5), (0, 1, 10)], 19)_

Example 2: Small graph with 5 vertices

   _Prim's MST: ([(0, 1, 2), (1, 2, 3), (1, 4, 5), (0, 3, 6)], 16)_

   _Kruskal's MST: ([(0, 1, 2), (1, 2, 3), (1, 4, 5), (0, 3, 6)], 16)_



### ***PERFORMANCE COMPARISON:***

Running performance test ...

Edge density: 0.3, Trials per size: 5

Vertices | Prim's Time (s) | Kruskal's Time (s) | Prim's Weight | Kruskal's Weight
----------------------------------------------------------------------
      10 | 0.000123 | 0.000098 | 123.4 | 123.4
      50 | 0.001234 | 0.001098 | 567.8 | 567.8
     100 | 0.003456 | 0.002876 | 1234.6 | 1234.6
     500 | 0.045678 | 0.038765 | 5678.2 | 5678.2


### ***CUSTOMOSING THE TEST:***

-> To modify the graph sizes for performance testing, edit the vertices_list in the if __name__ == "__main__": block.

-> To change the edge density (a value between 0 and 1), adjust the edge_density parameter in the run_performance_test call.

-> To increase the number of trials for more accurate timing, modify the trials parameter.


### ***PERFORMANCE ANALYSIS:***

-> Prim's Algorithm: Uses a priority queue (implemented with heapq) for an efficient O(E log V) time complexity, where E is the number of edges and V is the number of vertices.

-> It performs better on dense graphs due to its adjacency list representation.

-> Kruskal's Algorithm: Uses a union-find data structure with path compression and union by rank, achieving O(E log E) time complexity. It is typically faster for sparse graphs since it processes edges directly.

-> The performance test results will vary based on graph size and density.

-> Generally, Kruskal's algorithm may outperform Prim's on sparse graphs, while Prim's may be faster on dense graphs due to fewer priority queue operations.

-> Extending the Code:
-> To visualize the MST, you could extend the code with a library like matplotlib or networkx (not included here to keep dependencies minimal).

-> To test with specific graphs, modify the example graph creation in the if __name__ == "__main__": block or read graphs from a file.




## ***QUESTION 2***

### ***N-Queens Visualization***

### ***OVERVIEW***

-> This Python program visualizes solutions to the N-Queens problem using Pygame.

-> The N-Queens problem involves placing N queens on an NxN chessboard such that no two queens threaten each other. 

-> The program finds all possible solutions using backtracking and displays them interactively, allowing users to cycle through solutions. 

-> It also includes a performance analysis for different board sizes.



### ***FEATURES***

_Visualization: Displays an 8x8 chessboard with queens represented by the ♕ symbol._


_Interactive Navigation: Press the spacebar to cycle through all possible solutions._


_Performance Analysis: Measures and prints the number of solutions and time taken for board sizes from 4 to 12._


_Pyodide Compatibility: Runs in both browser (via Pyodide) and local Python environments._



### ***REQUIREMENTS***


-> _Python 3.7+_

-> _Pygame library (pip install pygame)_

-> For browser execution: _Pyodide environment_



-> Optional: _asyncio for asynchronous execution_


### ***HOW TO RUN***

***Local Execution:***

-> Ensure Pygame is installed: _pip install pygame_


***Run the script:*** python n_queens.py

-> A window will open showing the 8x8 chessboard with the first solution.

-> Press the spacebar to cycle through solutions.

->Close the window to exit.


***Browser Execution:***

-> Ensure the script is run in a Pyodide-compatible environment.

-> The visualization and interaction work the same as in local execution.



### ***CONTROLS***

_Spacebar: Cycle through different solutions for the 8x8 board._

_Close Window: Exit the program._



### ***PERFORMANCE ANALYSIS***

-> The program automatically runs a performance analysis for board sizes N=4 to N=12.

-> It prints the number of solutions and the time taken for each N to the console.

-> Results are stored in the performance_data global variable as a list of tuples (N, solutions_count, time_taken).



### ***CODE STRUCTURE***

_setup(): Initializes Pygame, sets up the display window, and defines global variables._


_is_safe(): Checks if a queen can be placed at a given position without conflicts._


_solve_n_queens(): Uses backtracking to find all solutions to the N-Queens problem._


_initialize_board(): Creates an NxN board initialized with zeros._


_analyze_performance(): Runs the solver for different board sizes and records performance metrics._


_draw_board(): Renders the chessboard and queens using Pygame._


_update_loop(): Handles events and updates the visualization asynchronously._


_main(): Orchestrates the program, solving the problem and running the visualization loop._



### ***NOTES***

-> The default board size is 8x8, but the performance analysis tests sizes up to 12x12.

-> The program uses a checkerboard pattern (white and black squares) for the board, with queens displayed in red.

-> The backtracking algorithm ensures all solutions are found efficiently.

-> The program is designed to avoid local file I/O and network calls for Pyodide compatibility.



### ***LIMITATIONS***

-> The visualization is fixed at 8x8 for simplicity; modifying board_size requires adjusting cell_size for proper display.

-> Performance analysis can be slow for larger N due to the exponential nature of the N-Queens problem.

-> No sound effects are included due to Pyodide limitations with pygame's sound handling.
