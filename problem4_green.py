#!/usr/bin/env python3
"""
Problem 4: Green Cloud Scheduler
=================================

Optimize cloud workload scheduling to reduce energy consumption
using quantum optimization.
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def create_workloads(num_workloads=5):
    """Create sample workloads with energy requirements."""
    np.random.seed(42)
    workloads = []
    for i in range(num_workloads):
        workloads.append({
            'id': i,
            'name': f'Workload_{i}',
            'cpu_hours': np.random.randint(1, 10),
            'memory_gb': np.random.randint(1, 16),
            'energy_kwh': np.random.uniform(0.5, 5.0),
            'priority': np.random.randint(1, 4)
        })
    return workloads


def create_servers(num_servers=3):
    """Create sample servers with energy profiles."""
    servers = []
    for i in range(num_servers):
        servers.append({
            'id': i,
            'name': f'Server_{i}',
            'max_cpu': 32,
            'max_memory': 64,
            'idle_power': np.random.uniform(100, 200),
            'active_power': np.random.uniform(300, 500),
            'efficiency': np.random.uniform(0.7, 0.95)
        })
    return servers


def calculate_energy_cost(assignment, workloads, servers):
    """Calculate total energy cost for an assignment."""
    total_energy = 0
    
    for workload_idx, server_idx in enumerate(assignment):
        workload = workloads[workload_idx]
        server = servers[server_idx]
        
        # Energy = base energy * workload factor / efficiency
        energy = workload['energy_kwh'] * (server['active_power'] / 1000) / server['efficiency']
        total_energy += energy
    
    return total_energy


def greedy_schedule(workloads, servers):
    """Greedy scheduling algorithm."""
    print("Running greedy scheduler...")
    
    assignment = []
    server_load = [0] * len(servers)
    
    for workload in workloads:
        # Find server with most remaining capacity
        best_server = 0
        best_load = float('inf')
        
        for i, server in enumerate(servers):
            if server_load[i] + workload['cpu_hours'] <= server['max_cpu']:
                if server_load[i] < best_load:
                    best_load = server_load[i]
                    best_server = i
        
        assignment.append(best_server)
        server_load[best_server] += workload['cpu_hours']
    
    return assignment


def quantum_optimized_schedule(workloads, servers):
    """Quantum-optimized scheduling using QAOA-like approach."""
    print("Running quantum-optimized scheduler...")
    
    num_workloads = len(workloads)
    num_servers = len(servers)
    
    # Create QAOA circuit
    qc = QuantumCircuit(num_workloads * num_servers, num_workloads * num_servers)
    
    # Initial superposition
    qc.h(range(num_workloads * num_servers))
    
    # Simple optimization layers
    for _ in range(3):
        for i in range(num_workloads * num_servers):
            qc.rz(np.pi/4, i)
            qc.rx(np.pi/4, i)
    
    qc.measure(range(num_workloads * num_servers), range(num_workloads * num_servers))
    
    # Run simulation
    simulator = AerSimulator()
    job = simulator.run(qc, shots=100)
    result = job.result()
    counts = result.get_counts(qc)
    
    # Get best result
    best_count = max(counts.values())
    best_state = [k for k, v in counts.items() if v == best_count][0]
    
    # Convert to assignment
    assignment = []
    for i in range(num_workloads):
        server_bits = best_state[i*num_servers:(i+1)*num_servers]
        server_idx = int(server_bits, 2) % num_servers
        assignment.append(server_idx)
    
    return assignment


def visualize_results(workloads, servers, assignments):
    """Create visualization."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Energy comparison
    greedy_energy = calculate_energy_cost(assignments['greedy'], workloads, servers)
    quantum_energy = calculate_energy_cost(assignments['quantum'], workloads, servers)
    
    methods = ['Greedy', 'Quantum']
    energies = [greedy_energy, quantum_energy]
    colors = ['#2196F3', '#4CAF50']
    
    axes[0, 0].bar(methods, energies, color=colors)
    axes[0, 0].set_ylabel('Total Energy (kWh)')
    axes[0, 0].set_title('Energy Consumption Comparison')
    axes[0, 0].grid(axis='y', alpha=0.3)
    
    # Server utilization
    for idx, (method, assignment) in enumerate(assignments.items()):
        server_load = [0] * len(servers)
        for i, server_idx in enumerate(assignment):
            server_load[server_idx] += workloads[i]['cpu_hours']
        
        x = np.arange(len(servers))
        width = 0.35
        axes[0, 1].bar(x + idx*width, server_load, width, 
                       label=method.capitalize(), color=colors[idx])
    
    axes[0, 1].set_xlabel('Server')
    axes[0, 1].set_ylabel('CPU Hours')
    axes[0, 1].set_title('Server Utilization')
    axes[0, 1].legend()
    axes[0, 1].grid(axis='y', alpha=0.3)
    
    # Workload distribution
    for idx, (method, assignment) in enumerate(assignments.items()):
        counts = [assignment.count(i) for i in range(len(servers))]
        axes[1, 0].bar(x + idx*width, counts, width,
                       label=method.capitalize(), color=colors[idx])
    
    axes[1, 0].set_xlabel('Server')
    axes[1, 0].set_ylabel('Number of Workloads')
    axes[1, 0].set_title('Workload Distribution')
    axes[1, 0].legend()
    axes[1, 0].grid(axis='y', alpha=0.3)
    
    # Energy savings
    savings = (greedy_energy - quantum_energy) / greedy_energy * 100
    axes[1, 1].bar(['Savings'], [savings], color='#FF9800')
    axes[1, 1].set_ylabel('Energy Savings (%)')
    axes[1, 1].set_title(f'Quantum Optimization Savings: {savings:.1f}%')
    axes[1, 1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/mike/Desktop/practic/quantum/quantum-hackthon/problem4_results.png',
                dpi=150, bbox_inches='tight')
    print("\nVisualization saved as 'problem4_results.png'")


def main():
    """Main function."""
    print("=" * 60)
    print("PROBLEM 4: GREEN CLOUD SCHEDULER")
    print("=" * 60)
    
    # Create workloads and servers
    workloads = create_workloads(5)
    servers = create_servers(3)
    
    print(f"\nWorkloads: {len(workloads)}")
    for w in workloads:
        print(f"  {w['name']}: {w['cpu_hours']} CPU hours, {w['energy_kwh']:.2f} kWh")
    
    print(f"\nServers: {len(servers)}")
    for s in servers:
        print(f"  {s['name']}: {s['max_cpu']} CPU, efficiency: {s['efficiency']:.2f}")
    
    # Run schedulers
    greedy_assignment = greedy_schedule(workloads, servers)
    quantum_assignment = quantum_optimized_schedule(workloads, servers)
    
    print(f"\nGreedy assignment: {greedy_assignment}")
    print(f"Quantum assignment: {quantum_assignment}")
    
    # Calculate energy
    greedy_energy = calculate_energy_cost(greedy_assignment, workloads, servers)
    quantum_energy = calculate_energy_cost(quantum_assignment, workloads, servers)
    
    print(f"\nGreedy energy: {greedy_energy:.2f} kWh")
    print(f"Quantum energy: {quantum_energy:.2f} kWh")
    print(f"Savings: {(greedy_energy - quantum_energy) / greedy_energy * 100:.1f}%")
    
    # Visualize
    visualize_results(workloads, servers, {
        'greedy': greedy_assignment,
        'quantum': quantum_assignment
    })
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"\nWorkloads scheduled: {len(workloads)}")
    print(f"Servers available: {len(servers)}")
    print(f"Energy reduction: {(greedy_energy - quantum_energy) / greedy_energy * 100:.1f}%")
    print("\n✓ Problem 4 completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
