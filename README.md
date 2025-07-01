QUSETION 1

PREREQUSITE:
-> Ensure you have Python 3.x installed on your system.
-> No external libraries are required as the code uses standard Python libraries (heapq, time, random, collections).

SETUP:
-> Save the code above in a file named mst_algorithms.py.
-> Open a terminal or command prompt in the directory containing mst_algorithms.py.

Running the Program:

Execute the script using the command:
python .py

The program will:

-> Run two example test cases with small graphs (4 and 5 vertices) and print the MST edges and total weights for both Prim's and Kruskal's algorithms.
-> Perform a performance comparison on randomly generated graphs with 10, 50, 100, and 500 vertices, using an edge density of 0.3 and averaging over 5 trials.

OUTPUT:
-> The output will include:
-> Results for the example graphs, showing the MST edges (as tuples of (u, v, weight)) and total weight.
-> A performance table comparing the average execution time and MST weight for Prim's and Kruskal's algorithms across different graph sizes. 

Example output format:
Example 1: Small graph with 4 vertices
Prim's MST: ([(0, 3, 5), (3, 2, 4), (0, 1, 10)], 19)
Kruskal's MST: ([(2, 3, 4), (0, 3, 5), (0, 1, 10)], 19)

Example 2: Small graph with 5 vertices
Prim's MST: ([(0, 1, 2), (1, 2, 3), (1, 4, 5), (0, 3, 6)], 16)
Kruskal's MST: ([(0, 1, 2), (1, 2, 3), (1, 4, 5), (0, 3, 6)], 16)

PERFORMANCE COMPARISON:

Running performance tests...
Edge density: 0.3, Trials per size: 5
Vertices | Prim's Time (s) | Kruskal's Time (s) | Prim's Weight | Kruskal's Weight
----------------------------------------------------------------------
      10 | 0.000123 | 0.000098 | 123.4 | 123.4
      50 | 0.001234 | 0.001098 | 567.8 | 567.8
     100 | 0.003456 | 0.002876 | 1234.6 | 1234.6
     500 | 0.045678 | 0.038765 | 5678.2 | 5678.2


CUSTOMOSING THE TEST:
-> To modify the graph sizes for performance testing, edit the vertices_list in the if __name__ == "__main__": block.
-> To change the edge density (a value between 0 and 1), adjust the edge_density parameter in the run_performance_test call.
-> To increase the number of trials for more accurate timing, modify the trials parameter.


PERFORMANCE ANALYSIS:
-> Prim's Algorithm: Uses a priority queue (implemented with heapq) for an efficient O(E log V) time complexity, where E is the number of edges and V is the number of vertices. It performs better on dense graphs due to its adjacency list representation.
-> Kruskal's Algorithm: Uses a union-find data structure with path compression and union by rank, achieving O(E log E) time complexity. It is typically faster for sparse graphs since it processes edges directly.
-> The performance test results will vary based on graph size and density. Generally, Kruskal's algorithm may outperform Prim's on sparse graphs, while Prim's may be faster on dense graphs due to fewer priority queue operations.
-> Extending the Code:
-> To visualize the MST, you could extend the code with a library like matplotlib or networkx (not included here to keep dependencies minimal).
-> To test with specific graphs, modify the example graph creation in the if __name__ == "__main__": block or read graphs from a file.
     
