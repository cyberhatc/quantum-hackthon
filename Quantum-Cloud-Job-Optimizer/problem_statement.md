# Problem 1: Quantum Cloud Job Optimizer

## Problem Statement

Quantum cloud computing providers offer multiple backends with varying capabilities. Developers need to select the optimal backend for their quantum circuits based on factors like execution time, queue depth, and output fidelity.

## Challenge

Given a set of quantum circuits, benchmark them across multiple simulated cloud backends and recommend the optimal backend for each circuit type.

## Requirements

1. **Backend Simulation**: Create multiple simulated quantum backends with different:
   - Processing speeds
   - Queue depths
   - Noise levels (affecting fidelity)

2. **Benchmarking**: For each circuit-backend pair, measure:
   - Execution time
   - Queue wait time
   - Output fidelity (closeness to ideal result)

3. **Optimization**: Recommend the best backend based on:
   - Fastest total execution time
   - Highest fidelity
   - Lowest queue depth

4. **Visualization**: Generate comparative charts showing:
   - Backend performance comparison
   - Circuit-specific recommendations
   - Trade-off analysis

## Input

- List of quantum circuits (Bell states, GHZ states, etc.)
- Multiple backend configurations with different capabilities

## Output

- Optimal backend recommendation for each circuit
- Performance comparison charts
- Benchmark statistics

## Evaluation Criteria

- Accuracy of backend recommendations
- Completeness of benchmarking metrics
- Quality of visualizations
- Code efficiency and documentation

## File

`problem1_optimizer.py`
