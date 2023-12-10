# Bellman-Ford Algorithm in Python

This repository contains an implementation of the Bellman-Ford Algorithm in Python for finding the shortest path from a specified source vertex to all other vertices in a weighted graph.

## Overview

The Bellman-Ford Algorithm is used to find the shortest paths from a single source vertex to all other vertices in a graph, even in the presence of negative edge weights. It iterates over all edges multiple times, relaxing them to find the shortest distances.

## How to Use

1. **Inputting the Graph:**
   - Run the Python script `bellman_ford.py`.
   - Enter the number of vertices and the number of edges in the graph.
   - Enter edges for the graph with weights in the format: `'source destination weight'`.

2. **Specifying Source Vertex:**
   - After entering the graph details, the program will prompt you to enter the source vertex.
   - Input the source vertex from which you want to find the shortest paths.

3. **Viewing Results:**
   - The program will display the shortest distances from the specified source vertex to all other vertices in the graph.

## Example Usage

```bash
$ python bellman_ford.py
Enter the number of vertices in the graph: 4
Enter the number of edges in the graph: 4
Enter edges for the graph with weights (format: 'source destination weight'):
0 1 4
0 2 3
1 2 -1
2 3 2
Enter the source vertex to find shortest paths from: 0

Shortest distances from vertex 0:
Vertex 0: Distance from source = 0
Vertex 1: Distance from source = 4
Vertex 2: Distance from source = 3
Vertex 3: Distance from source = 5
```

## Additional Notes

- The algorithm handles graphs with negative edge weights and can detect negative cycles.
- Adjust the input of edges and weights based on your specific graph requirements.
