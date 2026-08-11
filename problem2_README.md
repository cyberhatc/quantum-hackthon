# Problem 2: Hybrid Route Optimization (QAOA)

## Problem Statement

The Traveling Salesman Problem (TSP) is a classic optimization challenge. While classical algorithms can solve small instances, quantum approaches using QAOA (Quantum Approximate Optimization Algorithm) offer potential advantages for larger problem sizes.

## Challenge

Implement a hybrid quantum-classical approach to solve TSP for a set of cities, using QAOA for the quantum optimization component.

## Requirements

1. **Problem Encoding**: Encode TSP as a QUBO (Quadratic Unconstrained Binary Optimization) problem

2. **QAOA Implementation**: 
   - Create parameterized quantum circuit
   - Implement cost and mixer Hamiltonians
   - Classical optimization loop for parameter tuning

3. **Constraints**:
   - Each city visited exactly once
   - Return to starting city
   - Minimize total distance

4. **Visualization**:
   - City locations on 2D plane
   - Optimal route highlighting
   - Convergence plot of optimization

## Input

- List of city coordinates (x, y)
- Distance matrix between cities

## Output

- Optimal route order
- Total distance
- Visualization of route
- Optimization convergence history

## Evaluation Criteria

- Correctness of TSP solution
- Quality of QAOA implementation
- Visualization clarity
- Performance on different city counts

## File

`problem2_routing.py`
