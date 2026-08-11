#!/usr/bin/env python3
"""
Problem 6: Disaster Response Resource Allocation
=================================================

Optimize emergency resource allocation using quantum optimization.
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def create_disaster_scenario():
    """Create a disaster scenario with resources and needs."""
    np.random.seed(42)
    
    # Resources available
    resources = {
        'medical_kits': 50,
        'food_supplies': 100,
        'water_tanks': 30,
        'blankets': 200,
        'generators': 10
    }
    
    # Affected areas
    areas = [
        {'name': 'Downtown', 'population': 5000, 'severity': 0.8},
        {'name': 'Suburbs', 'population': 3000, 'severity': 0.5},
        {'name': 'Industrial', 'population': 1000, 'severity': 0.9},
        {'name': 'Riverside', 'population': 2000, 'severity': 0.6},
        {'name': 'Hillside', 'population': 1500, 'severity': 0.3}
    ]
    
    # Calculate needs for each area
    for area in areas:
        area['needs'] = {
            'medical_kits': int(area['population'] / 200 * area['severity']),
            'food_supplies': int(area['population'] / 50 * area['severity']),
            'water_tanks': int(area['population'] / 500 * area['severity']),
            'blankets': int(area['population'] / 30 * area['severity']),
            'generators': int(area['population'] / 1000 * area['severity'])
        }
    
    return resources, areas


def calculate_satisfaction(allocation, areas):
    """Calculate satisfaction score for an allocation."""
    total_satisfaction = 0
    
    for i, area in enumerate(areas):
        area_satisfaction = 0
        for resource, needed in area['needs'].items():
            allocated = allocation[i].get(resource, 0)
            if needed > 0:
                area_satisfaction += min(allocated / needed, 1.0)
        
        total_satisfaction += area_satisfaction * area['population']
    
    return total_satisfaction / sum(a['population'] for a in areas)


def greedy_allocation(resources, areas):
    """Greedy allocation based on severity."""
    print("Running greedy allocator...")
    
    allocation = [{} for _ in areas]
    remaining = resources.copy()
    
    # Sort areas by severity
    sorted_areas = sorted(enumerate(areas), key=lambda x: x[1]['severity'], reverse=True)
    
    for idx, area in sorted_areas:
        for resource, needed in area['needs'].items():
            available = remaining.get(resource, 0)
            allocated = min(needed, available)
            allocation[idx][resource] = allocated
            remaining[resource] = available - allocated
    
    return allocation


def quantum_allocation(resources, areas):
    """Quantum-optimized allocation."""
    print("Running quantum allocator...")
    
    num_areas = len(areas)
    num_resources = len(resources)
    
    # Create optimization circuit
    qc = QuantumCircuit(num_areas * num_resources, num_areas * num_resources)
    
    # Superposition
    qc.h(range(num_areas * num_resources))
    
    # Optimization layers
    for _ in range(3):
        for i in range(num_areas * num_resources):
            qc.rz(np.pi/4, i)
            qc.rx(np.pi/4, i)
    
    qc.measure(range(num_areas * num_resources), range(num_areas * num_resources))
    
    # Run
    simulator = AerSimulator()
    job = simulator.run(qc, shots=100)
    result = job.result()
    counts = result.get_counts(qc)
    
    # Get best
    best_count = max(counts.values())
    best_state = [k for k, v in counts.items() if v == best_count][0]
    
    # Convert to allocation
    allocation = [{} for _ in areas]
    resource_names = list(resources.keys())
    
    for i in range(num_areas):
        for j, resource in enumerate(resource_names):
            bit_idx = i * num_resources + j
            if best_state[bit_idx] == '1':
                allocation[i][resource] = min(
                    areas[i]['needs'][resource],
                    resources[resource] // num_areas
                )
            else:
                allocation[i][resource] = 0
    
    return allocation


def visualize_results(areas, allocations):
    """Create visualization."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Satisfaction comparison
    greedy_sat = calculate_satisfaction(allocations['greedy'], areas)
    quantum_sat = calculate_satisfaction(allocations['quantum'], areas)
    
    methods = ['Greedy', 'Quantum']
    satisfactions = [greedy_sat * 100, quantum_sat * 100]
    colors = ['#2196F3', '#4CAF50']
    
    axes[0, 0].bar(methods, satisfactions, color=colors)
    axes[0, 0].set_ylabel('Satisfaction (%)')
    axes[0, 0].set_title('Overall Satisfaction')
    axes[0, 0].set_ylim(0, 100)
    axes[0, 0].grid(axis='y', alpha=0.3)
    
    # Resource distribution
    resource_names = list(areas[0]['needs'].keys())
    x = np.arange(len(resource_names))
    width = 0.35
    
    greedy_totals = [sum(a.get(r, 0) for a in allocations['greedy']) for r in resource_names]
    quantum_totals = [sum(a.get(r, 0) for a in allocations['quantum']) for r in resource_names]
    
    axes[0, 1].bar(x - width/2, greedy_totals, width, label='Greedy', color='#2196F3')
    axes[0, 1].bar(x + width/2, quantum_totals, width, label='Quantum', color='#4CAF50')
    axes[0, 1].set_xlabel('Resource')
    axes[0, 1].set_ylabel('Total Allocated')
    axes[0, 1].set_title('Resource Allocation')
    axes[0, 1].set_xticks(x)
    axes[0, 1].set_xticklabels(resource_names, rotation=45)
    axes[0, 1].legend()
    axes[0, 1].grid(axis='y', alpha=0.3)
    
    # Area-by-area comparison
    area_names = [a['name'] for a in areas]
    greedy_area = [calculate_satisfaction([allocations['greedy'][i]], [areas[i]]) 
                   for i in range(len(areas))]
    quantum_area = [calculate_satisfaction([allocations['quantum'][i]], [areas[i]]) 
                    for i in range(len(areas))]
    
    x = np.arange(len(area_names))
    axes[1, 0].bar(x - width/2, greedy_area, width, label='Greedy', color='#2196F3')
    axes[1, 0].bar(x + width/2, quantum_area, width, label='Quantum', color='#4CAF50')
    axes[1, 0].set_xlabel('Area')
    axes[1, 0].set_ylabel('Satisfaction')
    axes[1, 0].set_title('Area-wise Satisfaction')
    axes[1, 0].set_xticks(x)
    axes[1, 0].set_xticklabels(area_names, rotation=45)
    axes[1, 0].legend()
    axes[1, 0].grid(axis='y', alpha=0.3)
    
    # Severity vs allocation
    severities = [a['severity'] for a in areas]
    axes[1, 1].scatter(severities, quantum_sat, s=100, c='#FF5722', label='Quantum')
    axes[1, 1].scatter(severities, greedy_sat, s=100, c='#2196F3', marker='x', label='Greedy')
    axes[1, 1].set_xlabel('Area Severity')
    axes[1, 1].set_ylabel('Satisfaction')
    axes[1, 1].set_title('Severity vs Satisfaction')
    axes[1, 1].legend()
    axes[1, 1].grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/mike/Desktop/practic/quantum/quantum-hackthon/problem6_results.png',
                dpi=150, bbox_inches='tight')
    print("\nVisualization saved as 'problem6_results.png'")


def main():
    """Main function."""
    print("=" * 60)
    print("PROBLEM 6: DISASTER RESPONSE RESOURCE ALLOCATION")
    print("=" * 60)
    
    # Create scenario
    resources, areas = create_disaster_scenario()
    
    print(f"\nResources: {resources}")
    print(f"\nAffected areas: {len(areas)}")
    for area in areas:
        print(f"  {area['name']}: pop={area['population']}, severity={area['severity']}")
    
    # Run allocators
    greedy_alloc = greedy_allocation(resources, areas)
    quantum_alloc = quantum_allocation(resources, areas)
    
    # Calculate satisfaction
    greedy_sat = calculate_satisfaction(greedy_alloc, areas)
    quantum_sat = calculate_satisfaction(quantum_alloc, areas)
    
    print(f"\nGreedy satisfaction: {greedy_sat*100:.1f}%")
    print(f"Quantum satisfaction: {quantum_sat*100:.1f}%")
    
    # Visualize
    visualize_results(areas, {'greedy': greedy_alloc, 'quantum': quantum_alloc})
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"\nAreas served: {len(areas)}")
    print(f"Resources allocated: {sum(resources.values())}")
    print(f"Satisfaction improvement: {(quantum_sat - greedy_sat) * 100:.1f}%")
    print("\n✓ Problem 6 completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
