#!/usr/bin/env python3
"""
Problem 2: Hybrid Quantum-Cloud Route Optimization
===================================================

Use QAOA with classical optimization to solve delivery routing.
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random
from itertools import permutations


def create_distance_matrix(num_locations):
    """Create a random distance matrix."""
    np.random.seed(42)
    matrix = np.random.randint(1, 20, size=(num_locations, num_locations))
    matrix = (matrix + matrix.T) // 2
    np.fill_diagonal(matrix, 0)
    return matrix


def calculate_route_distance(route, distance_matrix):
    """Calculate total distance for a route."""
    total = 0
    for i in range(len(route) - 1):
        total += distance_matrix[route[i], route[i+1]]
    total += distance_matrix[route[-1], route[0]]
    return total


def brute_force_tsp(distance_matrix):
    """Solve TSP using brute force (for small instances)."""
    num_locations = len(distance_matrix)
    locations = list(range(num_locations))
    
    best_cost = float('inf')
    best_route = None
    
    for perm in permutations(locations):
        cost = calculate_route_distance(list(perm), distance_matrix)
        if cost < best_cost:
            best_cost = cost
            best_route = list(perm)
    
    return best_route, best_cost


def create_qaoa_circuit(num_qubits, params):
    """Create a QAOA circuit."""
    qc = QuantumCircuit(num_qubits, num_qubits)
    
    # Initial superposition
    for i in range(num_qubits):
        qc.h(i)
    
    # Cost unitary
    gamma = params[0]
    for i in range(num_qubits):
        qc.rz(gamma, i)
    
    # Mixer unitary
    beta = params[1]
    for i in range(num_qubits):
        qc.rx(beta, i)
    
    qc.measure(range(num_qubits), range(num_qubits))
    return qc


def run_qaoa_simulation(distance_matrix, params):
    """Run QAOA simulation."""
    num_qubits = len(distance_matrix)
    qc = create_qaoa_circuit(num_qubits, params)
    
    simulator = AerSimulator()
    job = simulator.run(qc, shots=100)
    result = job.result()
    counts = result.get_counts(qc)
    
    # Get most frequent result
    best_count = max(counts.values())
    best_state = [k for k, v in counts.items() if v == best_count][0]
    
    # Convert to route (use binary as ordering hint)
    route = []
    for i, bit in enumerate(best_state[::-1]):
        if bit == '1':
            route.append(i)
    
    # Fill remaining locations
    for i in range(num_qubits):
        if i not in route:
            route.append(i)
    
    cost = calculate_route_distance(route, distance_matrix)
    return route, cost


def optimize_qaoa(distance_matrix, iterations=30):
    """Run QAOA optimization."""
    print("Running QAOA optimization...")
    
    best_cost = float('inf')
    best_route = None
    costs = []
    
    for i in range(iterations):
        gamma = random.uniform(0, 2 * np.pi)
        beta = random.uniform(0, np.pi)
        
        route, cost = run_qaoa_simulation(distance_matrix, [gamma, beta])
        costs.append(cost)
        
        if cost < best_cost:
            best_cost = cost
            best_route = route
        
        if (i + 1) % 10 == 0:
            print(f"  Iteration {i+1}: best cost = {best_cost}")
    
    return best_route, best_cost, costs


def visualize_results(route, distance_matrix, costs, optimal_cost):
    """Create visualization."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Cost over iterations
    axes[0].plot(costs, color='#2196F3', linewidth=2, label='QAOA')
    axes[0].axhline(y=optimal_cost, color='red', linestyle='--', label='Optimal')
    axes[0].set_xlabel('Iteration')
    axes[0].set_ylabel('Route Cost')
    axes[0].set_title('QAOA Optimization Progress')
    axes[0].legend()
    axes[0].grid(alpha=0.3)
    
    # Route segments
    segments = list(range(len(route)))
    distances = [distance_matrix[route[i], route[(i+1) % len(route)]] 
                for i in range(len(route))]
    
    axes[1].bar(segments, distances, color='#FF5722')
    axes[1].set_xlabel('Route Segment')
    axes[1].set_ylabel('Distance')
    axes[1].set_title(f'Optimized Route: {" → ".join(map(str, route))} → {route[0]}')
    axes[1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/mike/Desktop/practic/quantum/quantum-hackthon/problem2_results.png',
                dpi=150, bbox_inches='tight')
    print("\nVisualization saved as 'problem2_results.png'")


def main():
    """Main function."""
    print("=" * 60)
    print("PROBLEM 2: HYBRID QUANTUM-CLOUD ROUTE OPTIMIZATION")
    print("=" * 60)
    
    # Create distance matrix
    num_locations = 5
    distance_matrix = create_distance_matrix(num_locations)
    
    print(f"\nDistance matrix ({num_locations} locations):")
    print(distance_matrix)
    
    # Find optimal solution (brute force for comparison)
    optimal_route, optimal_cost = brute_force_tsp(distance_matrix)
    print(f"\nOptimal route (brute force): {optimal_route}")
    print(f"Optimal cost: {optimal_cost}")
    
    # Run QAOA
    qaoa_route, qaoa_cost, costs = optimize_qaoa(distance_matrix)
    
    print(f"\nQAOA route: {qaoa_route}")
    print(f"QAOA cost: {qaoa_cost}")
    
    # Visualize
    visualize_results(qaoa_route, distance_matrix, costs, optimal_cost)
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"\nOptimal route: {optimal_route} (cost: {optimal_cost})")
    print(f"QAOA route: {qaoa_route} (cost: {qaoa_cost})")
    print(f"Gap: {((qaoa_cost - optimal_cost) / optimal_cost * 100):.1f}%")
    print("\n✓ Problem 2 completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
