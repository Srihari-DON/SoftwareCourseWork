# Algorithms

Collection of fundamental algorithms with implementations, explanations, and analysis.

## 📂 Categories

### Sorting Algorithms
- **Bubble Sort** - Simple comparison-based sorting
- **Selection Sort** - In-place comparison sorting
- **Insertion Sort** - Efficient for small datasets
- **Merge Sort** - Divide and conquer approach
- **Quick Sort** - Efficient average-case performance
- **Heap Sort** - Heap-based sorting algorithm

### Searching Algorithms
- **Linear Search** - Sequential search through array
- **Binary Search** - Logarithmic search in sorted array
- **Depth-First Search (DFS)** - Graph traversal algorithm
- **Breadth-First Search (BFS)** - Level-order graph traversal

### Dynamic Programming
- **Fibonacci Sequence** - Classic DP example
- **Knapsack Problem** - Optimization problem
- **Longest Common Subsequence** - String comparison
- **Edit Distance** - String similarity metric

### Graph Algorithms
- **Dijkstra's Algorithm** - Shortest path in weighted graphs
- **Bellman-Ford Algorithm** - Shortest path with negative weights
- **Floyd-Warshall Algorithm** - All-pairs shortest paths
- **Kruskal's Algorithm** - Minimum spanning tree

## 📊 Complexity Analysis

Each algorithm includes:
- **Time Complexity**: Best, Average, and Worst case
- **Space Complexity**: Additional memory requirements
- **Stability**: Maintains relative order of equal elements
- **In-place**: Whether it modifies the input array

## 🎯 Learning Objectives

- Understand algorithm design paradigms
- Analyze time and space complexity
- Choose appropriate algorithms for specific problems
- Implement efficient solutions

## 📁 Structure

```
algorithms/
├── sorting/         # Sorting algorithm implementations
├── searching/       # Search algorithm implementations
├── graph/           # Graph algorithms
├── dynamic/         # Dynamic programming solutions
├── greedy/          # Greedy algorithm examples
└── tests/           # Comprehensive test suites
```

## 🔍 Quick Reference

| Algorithm | Time Complexity | Space Complexity | Stable | In-place |
|-----------|----------------|------------------|---------|----------|
| Bubble Sort | O(n²) | O(1) | Yes | Yes |
| Merge Sort | O(n log n) | O(n) | Yes | No |
| Quick Sort | O(n log n) avg | O(log n) | No | Yes |
| Binary Search | O(log n) | O(1) | - | Yes |