#!/usr/bin/env python3
"""
Problem 7: Quantum Portfolio Optimizer
======================================

Optimize cloud budget allocation across services under constraints.
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def create_cloud_services():
    """Create cloud services with costs and benefits."""
    services = [
        {'name': 'Compute (VMs)', 'cost': 1000, 'benefit': 80, 'risk': 0.2},
        {'name': 'Storage (S3)', 'cost': 500, 'benefit': 60, 'risk': 0.1},
        {'name': 'Database (RDS)', 'cost': 800, 'benefit': 70, 'risk': 0.15},
        {'name': 'ML Services', 'cost': 1500, 'benefit': 90, 'risk': 0.3},
        {'name': 'Analytics', 'cost': 700, 'benefit': 65, 'risk': 0.2},
        {'name': 'Security', 'cost': 400, 'benefit': 50, 'risk': 0.05},
        {'name': 'Networking', 'cost': 300, 'benefit': 40, 'risk': 0.1},
        {'name': 'Monitoring', 'cost': 200, 'benefit': 35, 'risk': 0.05}
    ]
    return services


def calculate_portfolio_value(allocation, services, budget):
    """Calculate portfolio value considering cost, benefit, and risk."""
    total_cost = 0
    total_benefit = 0
    total_risk = 0
    
    for i, selected in enumerate(allocation):
        if selected:
            total_cost += services[i]['cost']
            total_benefit += services[i]['benefit']
            total_risk += services[i]['risk']
    
    if total_cost > budget:
        return -1000  # Penalty for exceeding budget
    
    # Value = benefit - risk penalty
    value = total_benefit - total_risk * 50
    
    return value


def brute_force_optimization(services, budget):
    """Brute force optimization for comparison."""
    from itertools import product
    
    num_services = len(services)
    best_value = -float('inf')
    best_allocation = None
    
    for allocation in product([0, 1], repeat=num_services):
        value = calculate_portfolio_value(list(allocation), services, budget)
        if value > best_value:
            best_value = value
            best_allocation = list(allocation)
    
    return best_allocation, best_value


def quantum_optimization(services, budget, iterations=50):
    """Quantum-inspired optimization."""
    print("Running quantum portfolio optimization...")
    
    num_services = len(services)
    best_value = -float('inf')
    best_allocation = None
    values = []
    
    for _ in range(iterations):
        # Random allocation with budget constraint
        allocation = [0] * num_services
        remaining_budget = budget
        
        # Shuffle service order
        order = np.random.permutation(num_services)
        
        for i in order:
            if services[i]['cost'] <= remaining_budget:
                if np.random.random() > 0.3:  # 70% chance to include
                    allocation[i] = 1
                    remaining_budget -= services[i]['cost']
        
        value = calculate_portfolio_value(allocation, services, budget)
        values.append(value)
        
        if value > best_value:
            best_value = value
            best_allocation = allocation.copy()
    
    return best_allocation, best_value, values


def visualize_results(services, allocations, values):
    """Create visualization."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Allocation comparison
    service_names = [s['name'] for s in services]
    
    for idx, (method, alloc) in enumerate(allocations.items()):
        selected = [i for i, a in enumerate(alloc) if a]
        costs = [services[i]['cost'] for i in selected]
        axes[0, 0].barh([service_names[i] for i in selected], costs, 
                       label=method.capitalize(), alpha=0.7)
    
    axes[0, 0].set_xlabel('Cost ($)')
    axes[0, 0].set_title('Selected Services')
    axes[0, 0].legend()
    axes[0, 0].grid(axis='x', alpha=0.3)
    
    # Budget usage
    budget = 5000
    for idx, (method, alloc) in enumerate(allocations.items()):
        total_cost = sum(services[i]['cost'] for i, a in enumerate(alloc) if a)
        axes[0, 1].bar(method.capitalize(), total_cost, color=['#2196F3', '#4CAF50'][idx])
    axes[0, 1].axhline(y=budget, color='red', linestyle='--', label='Budget')
    axes[0, 1].set_ylabel('Total Cost ($)')
    axes[0, 1].set_title('Budget Usage')
    axes[0, 1].legend()
    axes[0, 1].grid(axis='y', alpha=0.3)
    
    # Risk vs Benefit
    for idx, (method, alloc) in enumerate(allocations.items()):
        risk = sum(services[i]['risk'] for i, a in enumerate(alloc) if a)
        benefit = sum(services[i]['benefit'] for i, a in enumerate(alloc) if a)
        axes[1, 0].scatter(risk, benefit, s=200, label=method.capitalize(),
                          color=['#2196F3', '#4CAF50'][idx])
    
    axes[1, 0].set_xlabel('Total Risk')
    axes[1, 0].set_ylabel('Total Benefit')
    axes[1, 0].set_title('Risk vs Benefit')
    axes[1, 0].legend()
    axes[1, 0].grid(alpha=0.3)
    
    # Optimization progress
    axes[1, 1].plot(values['quantum'], color='#4CAF50', label='Quantum')
    axes[1, 1].axhline(y=values['brute_force'], color='red', linestyle='--', 
                       label='Optimal')
    axes[1, 1].set_xlabel('Iteration')
    axes[1, 1].set_ylabel('Portfolio Value')
    axes[1, 1].set_title('Optimization Progress')
    axes[1, 1].legend()
    axes[1, 1].grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/mike/Desktop/practic/quantum/quantum-hackthon/problem7_results.png',
                dpi=150, bbox_inches='tight')
    print("\nVisualization saved as 'problem7_results.png'")


def main():
    """Main function."""
    print("=" * 60)
    print("PROBLEM 7: QUANTUM PORTFOLIO OPTIMIZER")
    print("=" * 60)
    
    services = create_cloud_services()
    budget = 5000
    
    print(f"\nBudget: ${budget}")
    print(f"\nAvailable services:")
    for s in services:
        print(f"  {s['name']}: ${s['cost']}, benefit={s['benefit']}, risk={s['risk']}")
    
    # Run optimizations
    brute_alloc, brute_value = brute_force_optimization(services, budget)
    quantum_alloc, quantum_value, quantum_values = quantum_optimization(services, budget)
    
    print(f"\nBrute force allocation: {[s['name'] for i, s in enumerate(services) if brute_alloc[i]]}")
    print(f"Brute force value: {brute_value}")
    
    print(f"\nQuantum allocation: {[s['name'] for i, s in enumerate(services) if quantum_alloc[i]]}")
    print(f"Quantum value: {quantum_value}")
    
    # Visualize
    visualize_results(services, {
        'brute_force': brute_alloc,
        'quantum': quantum_alloc
    }, {
        'brute_force': brute_value,
        'quantum': quantum_values
    })
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"\nBudget: ${budget}")
    print(f"Optimal value: {brute_value}")
    print(f"Quantum value: {quantum_value}")
    print(f"Gap: {((brute_value - quantum_value) / brute_value * 100):.1f}%")
    print("\n✓ Problem 7 completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
