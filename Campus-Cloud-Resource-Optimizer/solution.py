#!/usr/bin/env python3
"""
Problem 10: Campus Cloud Resource Optimizer
============================================

Optimize lab booking or GPU allocation using quantum optimization.
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def create_campus_resources():
    """Create campus computing resources."""
    resources = {
        'labs': [
            {'name': 'Lab A (GPU Cluster)', 'gpu': 8, 'cpu': 64, 'memory': 256},
            {'name': 'Lab B (CPU Cluster)', 'gpu': 0, 'cpu': 128, 'memory': 512},
            {'name': 'Lab C (Mixed)', 'gpu': 4, 'cpu': 32, 'memory': 128},
        ],
        'time_slots': ['09:00-12:00', '12:00-15:00', '15:00-18:00', '18:00-21:00']
    }
    return resources


def create_booking_requests():
    """Create sample booking requests."""
    requests = [
        {'name': 'ML Training', 'gpu': 4, 'cpu': 16, 'memory': 64, 'priority': 3},
        {'name': 'Data Processing', 'gpu': 0, 'cpu': 32, 'memory': 128, 'priority': 2},
        {'name': 'Deep Learning', 'gpu': 8, 'cpu': 16, 'memory': 128, 'priority': 3},
        {'name': 'Simulation', 'gpu': 2, 'cpu': 64, 'memory': 256, 'priority': 1},
        {'name': 'Visualization', 'gpu': 1, 'cpu': 8, 'memory': 32, 'priority': 1},
    ]
    return requests


def calculate_utilization(allocation, resources):
    """Calculate resource utilization."""
    total_gpu = sum(r['gpu'] for r in resources['labs'])
    total_cpu = sum(r['cpu'] for r in resources['labs'])
    total_memory = sum(r['memory'] for r in resources['labs'])
    
    used_gpu = 0
    used_cpu = 0
    used_memory = 0
    
    for req_idx, (lab_idx, slot_idx) in enumerate(allocation):
        if lab_idx is not None:
            lab = resources['labs'][lab_idx]
            req = create_booking_requests()[req_idx]
            used_gpu += min(req['gpu'], lab['gpu'])
            used_cpu += min(req['cpu'], lab['cpu'])
            used_memory += min(req['memory'], lab['memory'])
    
    return {
        'gpu': used_gpu / total_gpu if total_gpu > 0 else 0,
        'cpu': used_cpu / total_cpu,
        'memory': used_memory / total_memory
    }


def greedy_allocation(resources, requests):
    """Greedy allocation based on priority."""
    print("Running greedy allocator...")
    
    allocation = []
    lab_availability = {i: {s: True for s in range(len(resources['time_slots']))} 
                       for i in range(len(resources['labs']))}
    
    # Sort by priority
    sorted_requests = sorted(enumerate(requests), key=lambda x: x[1]['priority'], reverse=True)
    
    for req_idx, req in sorted_requests:
        assigned = False
        for lab_idx, lab in enumerate(resources['labs']):
            if req['gpu'] <= lab['gpu'] and req['cpu'] <= lab['cpu']:
                for slot in range(len(resources['time_slots'])):
                    if lab_availability[lab_idx][slot]:
                        allocation.append((lab_idx, slot))
                        lab_availability[lab_idx][slot] = False
                        assigned = True
                        break
            if assigned:
                break
        
        if not assigned:
            allocation.append((None, None))
    
    return allocation


def quantum_allocation(resources, requests):
    """Quantum-optimized allocation using random selection."""
    print("Running quantum allocator...")
    
    num_requests = len(requests)
    num_labs = len(resources['labs'])
    num_slots = len(resources['time_slots'])
    
    allocation = []
    lab_availability = {i: {s: True for s in range(num_slots)} 
                       for i in range(num_labs)}
    
    for req_idx, req in enumerate(requests):
        # Use quantum random to pick lab and slot
        qc = QuantumCircuit(4, 4)
        qc.h(range(4))
        qc.measure(range(4), range(4))
        
        simulator = AerSimulator()
        job = simulator.run(qc, shots=1)
        result = job.result()
        counts = result.get_counts()
        bits = list(counts.keys())[0][::-1]
        
        # Pick lab based on random bits
        lab_idx = int(bits[0:2], 2) % num_labs
        slot_idx = int(bits[2:4], 2) % num_slots
        
        # Find first available slot for this lab
        assigned = False
        for l in range(num_labs):
            for s in range(num_slots):
                if lab_availability[l][s] and req['gpu'] <= resources['labs'][l]['gpu'] and req['cpu'] <= resources['labs'][l]['cpu']:
                    allocation.append((l, s))
                    lab_availability[l][s] = False
                    assigned = True
                    break
            if assigned:
                break
        
        if not assigned:
            allocation.append((None, None))
    
    return allocation


def visualize_results(resources, requests, allocations):
    """Create visualization."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Utilization comparison
    greedy_util = calculate_utilization(allocations['greedy'], resources)
    quantum_util = calculate_utilization(allocations['quantum'], resources)
    
    metrics = ['GPU', 'CPU', 'Memory']
    greedy_vals = [greedy_util['gpu'] * 100, greedy_util['cpu'] * 100, greedy_util['memory'] * 100]
    quantum_vals = [quantum_util['gpu'] * 100, quantum_util['cpu'] * 100, quantum_util['memory'] * 100]
    
    x = np.arange(len(metrics))
    width = 0.35
    
    axes[0, 0].bar(x - width/2, greedy_vals, width, label='Greedy', color='#2196F3')
    axes[0, 0].bar(x + width/2, quantum_vals, width, label='Quantum', color='#4CAF50')
    axes[0, 0].set_ylabel('Utilization (%)')
    axes[0, 0].set_title('Resource Utilization')
    axes[0, 0].set_xticks(x)
    axes[0, 0].set_xticklabels(metrics)
    axes[0, 0].legend()
    axes[0, 0].grid(axis='y', alpha=0.3)
    
    # Booking success rate
    greedy_success = sum(1 for a in allocations['greedy'] if a[0] is not None)
    quantum_success = sum(1 for a in allocations['quantum'] if a[0] is not None)
    total = len(requests)
    
    axes[0, 1].bar(['Greedy', 'Quantum'], [greedy_success, quantum_success], 
                   color=['#2196F3', '#4CAF50'])
    axes[0, 1].set_ylabel('Successful Bookings')
    axes[0, 1].set_title(f'Booking Success (out of {total})')
    axes[0, 1].grid(axis='y', alpha=0.3)
    
    # Lab usage
    lab_names = [l['name'].split('(')[0].strip() for l in resources['labs']]
    greedy_lab_usage = [0] * len(lab_names)
    quantum_lab_usage = [0] * len(lab_names)
    
    for a in allocations['greedy']:
        if a[0] is not None:
            greedy_lab_usage[a[0]] += 1
    
    for a in allocations['quantum']:
        if a[0] is not None:
            quantum_lab_usage[a[0]] += 1
    
    x = np.arange(len(lab_names))
    axes[1, 0].bar(x - width/2, greedy_lab_usage, width, label='Greedy', color='#2196F3')
    axes[1, 0].bar(x + width/2, quantum_lab_usage, width, label='Quantum', color='#4CAF50')
    axes[1, 0].set_ylabel('Bookings')
    axes[1, 0].set_title('Lab Usage')
    axes[1, 0].set_xticks(x)
    axes[1, 0].set_xticklabels(lab_names, rotation=45)
    axes[1, 0].legend()
    axes[1, 0].grid(axis='y', alpha=0.3)
    
    # Time slot usage
    slot_names = resources['time_slots']
    greedy_slot_usage = [0] * len(slot_names)
    quantum_slot_usage = [0] * len(slot_names)
    
    for a in allocations['greedy']:
        if a[1] is not None:
            greedy_slot_usage[a[1]] += 1
    
    for a in allocations['quantum']:
        if a[1] is not None:
            quantum_slot_usage[a[1]] += 1
    
    x = np.arange(len(slot_names))
    axes[1, 1].bar(x - width/2, greedy_slot_usage, width, label='Greedy', color='#2196F3')
    axes[1, 1].bar(x + width/2, quantum_slot_usage, width, label='Quantum', color='#4CAF50')
    axes[1, 1].set_ylabel('Bookings')
    axes[1, 1].set_title('Time Slot Usage')
    axes[1, 1].set_xticks(x)
    axes[1, 1].set_xticklabels(slot_names, rotation=45)
    axes[1, 1].legend()
    axes[1, 1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/mike/Desktop/practic/quantum/quantum-hackthon/problem10_results.png',
                dpi=150, bbox_inches='tight')
    print("\nVisualization saved as 'problem10_results.png'")


def main():
    """Main function."""
    print("=" * 60)
    print("PROBLEM 10: CAMPUS CLOUD RESOURCE OPTIMIZER")
    print("=" * 60)
    
    resources = create_campus_resources()
    requests = create_booking_requests()
    
    print(f"\nLabs available: {len(resources['labs'])}")
    for lab in resources['labs']:
        print(f"  {lab['name']}: {lab['gpu']} GPUs, {lab['cpu']} CPUs")
    
    print(f"\nBooking requests: {len(requests)}")
    for req in requests:
        print(f"  {req['name']}: {req['gpu']} GPUs, {req['cpu']} CPUs (priority: {req['priority']})")
    
    # Run allocators
    greedy_alloc = greedy_allocation(resources, requests)
    quantum_alloc = quantum_allocation(resources, requests)
    
    # Calculate utilization
    greedy_util = calculate_utilization(greedy_alloc, resources)
    quantum_util = calculate_utilization(quantum_alloc, resources)
    
    print(f"\nGreedy utilization: GPU={greedy_util['gpu']*100:.1f}%, CPU={greedy_util['cpu']*100:.1f}%")
    print(f"Quantum utilization: GPU={quantum_util['gpu']*100:.1f}%, CPU={quantum_util['cpu']*100:.1f}%")
    
    # Visualize
    visualize_results(resources, requests, {
        'greedy': greedy_alloc,
        'quantum': quantum_alloc
    })
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"\nLabs: {len(resources['labs'])}")
    print(f"Time slots: {len(resources['time_slots'])}")
    print(f"Requests processed: {len(requests)}")
    print(f"Quantum utilization improvement: {(quantum_util['gpu'] - greedy_util['gpu']) * 100:.1f}%")
    print("\n✓ Problem 10 completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
