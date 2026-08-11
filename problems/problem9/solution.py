#!/usr/bin/env python3
"""
Problem 9: Quantum Circuit Marketplace
=======================================

Cloud platform where users share, benchmark and compare quantum circuits.
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import json


def create_sample_circuits():
    """Create sample quantum circuits for marketplace."""
    circuits = []
    
    # Bell State
    qc1 = QuantumCircuit(2, 2, name="Bell State")
    qc1.h(0)
    qc1.cx(0, 1)
    qc1.measure([0, 1], [0, 1])
    circuits.append({
        'name': 'Bell State',
        'description': 'Creates entangled qubits',
        'circuit': qc1,
        'qubits': 2,
        'gates': 2,
        'category': 'entanglement'
    })
    
    # GHZ State
    qc2 = QuantumCircuit(3, 3, name="GHZ State")
    qc2.h(0)
    qc2.cx(0, 1)
    qc2.cx(1, 2)
    qc2.measure([0, 1, 2], [0, 1, 2])
    circuits.append({
        'name': 'GHZ State',
        'description': 'Three-qubit entanglement',
        'circuit': qc2,
        'qubits': 3,
        'gates': 3,
        'category': 'entanglement'
    })
    
    # Quantum Fourier Transform (simplified)
    qc3 = QuantumCircuit(3, 3, name="QFT")
    qc3.h(0)
    qc3.cp(np.pi/2, 0, 1)
    qc3.cp(np.pi/4, 0, 2)
    qc3.h(1)
    qc3.cp(np.pi/2, 1, 2)
    qc3.h(2)
    qc3.measure([0, 1, 2], [0, 1, 2])
    circuits.append({
        'name': 'Quantum Fourier Transform',
        'description': 'QFT circuit for period finding',
        'circuit': qc3,
        'qubits': 3,
        'gates': 6,
        'category': 'algorithm'
    })
    
    # Grover's Oracle (2 qubit)
    qc4 = QuantumCircuit(2, 2, name="Grover Oracle")
    qc4.h(0)
    qc4.h(1)
    qc4.cz(0, 1)  # Oracle
    qc4.h(0)
    qc4.h(1)
    qc4.x(0)
    qc4.x(1)
    qc4.cz(0, 1)  # Diffusion
    qc4.x(0)
    qc4.x(1)
    qc4.h(0)
    qc4.h(1)
    qc4.measure([0, 1], [0, 1])
    circuits.append({
        'name': "Grover's Search",
        'description': "Grover's search algorithm",
        'circuit': qc4,
        'qubits': 2,
        'gates': 9,
        'category': 'algorithm'
    })
    
    return circuits


def benchmark_circuit(circuit, shots=1024):
    """Benchmark a quantum circuit."""
    simulator = AerSimulator()
    
    # Run circuit
    job = simulator.run(circuit['circuit'], shots=shots)
    result = job.result()
    counts = result.get_counts(circuit['circuit'])
    
    # Calculate metrics
    total_shots = sum(counts.values())
    unique_states = len(counts)
    entropy = -sum((v/total_shots) * np.log2(v/total_shots) for v in counts.values())
    
    # Execution time (simulated)
    import time
    start = time.time()
    for _ in range(10):
        simulator.run(circuit['circuit'], shots=100)
    avg_time = (time.time() - start) / 10
    
    return {
        'name': circuit['name'],
        'counts': counts,
        'unique_states': unique_states,
        'entropy': entropy,
        'avg_execution_time': avg_time,
        'fidelity': 1.0 - (unique_states / (2 ** circuit['qubits']))
    }


def compare_circuits(benchmarks):
    """Compare circuit performance."""
    print("\nCircuit Comparison:")
    print("-" * 60)
    
    for bm in benchmarks:
        print(f"\n{bm['name']}:")
        print(f"  Unique states: {bm['unique_states']}")
        print(f"  Entropy: {bm['entropy']:.3f}")
        print(f"  Avg execution time: {bm['avg_execution_time']:.4f}s")
        print(f"  Fidelity: {bm['fidelity']*100:.1f}%")


def visualize_results(circuits, benchmarks):
    """Create visualization."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    names = [c['name'] for c in circuits]
    
    # Qubit count comparison
    qubits = [c['qubits'] for c in circuits]
    axes[0, 0].barh(names, qubits, color='#2196F3')
    axes[0, 0].set_xlabel('Number of Qubits')
    axes[0, 0].set_title('Circuit Complexity (Qubits)')
    axes[0, 0].grid(axis='x', alpha=0.3)
    
    # Gate count comparison
    gates = [c['gates'] for c in circuits]
    axes[0, 1].barh(names, gates, color='#FF5722')
    axes[0, 1].set_xlabel('Number of Gates')
    axes[0, 1].set_title('Circuit Complexity (Gates)')
    axes[0, 1].grid(axis='x', alpha=0.3)
    
    # Entropy comparison
    entropies = [b['entropy'] for b in benchmarks]
    axes[1, 0].barh(names, entropies, color='#4CAF50')
    axes[1, 0].set_xlabel('Entropy (bits)')
    axes[1, 0].set_title('Output Distribution Entropy')
    axes[1, 0].grid(axis='x', alpha=0.3)
    
    # Execution time comparison
    times = [b['avg_execution_time'] * 1000 for b in benchmarks]  # Convert to ms
    axes[1, 1].barh(names, times, color='#FF9800')
    axes[1, 1].set_xlabel('Execution Time (ms)')
    axes[1, 1].set_title('Average Execution Time')
    axes[1, 1].grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/mike/Desktop/practic/quantum/quantum-hackthon/problem9_results.png',
                dpi=150, bbox_inches='tight')
    print("\nVisualization saved as 'problem9_results.png'")


def main():
    """Main function."""
    print("=" * 60)
    print("PROBLEM 9: QUANTUM CIRCUIT MARKETPLACE")
    print("=" * 60)
    
    # Create sample circuits
    circuits = create_sample_circuits()
    
    print(f"\nMarketplace contains {len(circuits)} circuits:")
    for c in circuits:
        print(f"  - {c['name']}: {c['description']}")
    
    # Benchmark all circuits
    print("\nBenchmarking circuits...")
    benchmarks = []
    for circuit in circuits:
        bm = benchmark_circuit(circuit)
        benchmarks.append(bm)
    
    # Compare
    compare_circuits(benchmarks)
    
    # Visualize
    visualize_results(circuits, benchmarks)
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"\nCircuits in marketplace: {len(circuits)}")
    print(f"Categories: {set(c['category'] for c in circuits)}")
    print(f"Total qubits used: {sum(c['qubits'] for c in circuits)}")
    print(f"Total gates used: {sum(c['gates'] for c in circuits)}")
    print("\n✓ Problem 9 completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
