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




# ***KRUSKAL'S ALGORITHM FOR MINIMUM SPANNING TREE (MST)***

This Python project implements **Kruskal's Algorithm** to find the Minimum Spanning Tree (MST) of an undirected weighted graph and visualizes both the original graph and the MST using `matplotlib` and `networkx`.

### ***Table of Contents***
- [Description](#description)
- [Features](#features)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Example Output](#example-output)
- [Contributing](#contributing)
- [License](#license)

### ***DESCRIPTION***
-> The script constructs a weighted undirected graph with 5 vertices (`A`, `B`, `C`, `D`, `E`) and 7 edges, applies Kruskal's Algorithm to compute the MST, and visualizes both the original graph and the MST side by side.
  
-> Kruskal's Algorithm selects edges in increasing order of weight, ensuring no cycles are formed, to create a tree that connects all vertices with the minimum total edge weight.

### ***FEATURES***
- Implements Kruskal's Algorithm using a **Disjoint-Set** data structure for cycle detection.
- Visualizes the original graph and the MST using `networkx` and `matplotlib`.
- Displays edge weights on both graphs.
- Uses a consistent layout for clear comparison between the original graph and MST.

### ***DEPENDENCIES***
- Python 3.x
- `matplotlib` (for plotting)
- `networkx` (for graph creation and manipulation)

### ***INSTALLATION***
1. Ensure Python 3.x is installed on your system.
2. Install the required packages using pip:
   ```bash
   pip install matplotlib networkx

    Clone or download this repository to your local machine.

### ***USAGE***

    Save the script as kruskal_mst.py.
    Run the script:
    bash

    python kruskal_mst.py
    A plot window will display two graphs:
        Left: The original graph with light blue nodes and default edges.
        Right: The MST with light green nodes and green edges. Edge weights are shown on both graphs.

-> To modify the graph, edit the vertices and edges lists in the script:

    vertices: List of node names (e.g., ['A', 'B', 'C', 'D', 'E']).
    edges: List of tuples (vertex1, vertex2, weight) (e.g., [('A', 'B', 1), ('A', 'C', 3)]).

### ***CODE STRUCTURE***

    -Imports: matplotlib.pyplot and networkx for visualization and graph handling.
    -Graph Definition: Defines vertices and weighted edges.
    -Edge Class: Represents an edge with vertices and weight, enabling sorting by weight.
    -DisjointSet Class: Implements Union-Find with path compression for cycle detection.
    -kruskal_mst Function: Computes the MST using Kruskal's Algorithm.
    -isualization: Creates side-by-side plots of the original graph and MST.

### ***EXAMPLE OUTPUT***

-> The script generates a plot with two subplots:

    Original Graph: Shows all vertices and edges with weights (e.g., edge A-B with weight 1).
    MST: Shows only the edges selected by Kruskal's Algorithm, forming a tree with the minimum total weight.

-> For the provided graph, the MST includes edges like A-B, B-C, C-E, and C-D, depending on the weights.


### ***CONTRIBUTING***

-> Contributions are welcome! Please:

    Fork the repository.
    Create a new branch for your feature or bug fix.
    Submit a pull request with a clear description of your changes.

### ***LICENSE***

-> This project is licensed under the MIT License. See the LICENSE file for details.
text
### ***Notes***
- The README assumes a standard project structure and includes a generic MIT license reference. If you have a specific license or additional project details, let me know, and I can update the README.
- The commented code improves readability for developers by explaining each section and key operations.
- The visualization uses `spring_layout` with a fixed seed for reproducibility, but you can modify the layout or styling (e.g., colors, node sizes) as needed.
- If you want to add more features (e.g., saving the plot, handling larger
