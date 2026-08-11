#!/usr/bin/env python3
"""
Problem 8: Quantum Password Strength Analyzer
==============================================

Evaluate passwords and generate entropy using QRNG simulation.
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math
import string


def generate_quantum_random(num_bits):
    """Generate random bits using quantum measurement."""
    qc = QuantumCircuit(num_bits, num_bits)
    qc.h(range(num_bits))
    qc.measure(range(num_bits), range(num_bits))
    
    simulator = AerSimulator()
    job = simulator.run(qc, shots=1)
    result = job.result()
    counts = result.get_counts()
    
    bitstring = list(counts.keys())[0]
    return [int(b) for b in bitstring[::-1]]


def calculate_password_entropy(password):
    """Calculate password entropy."""
    charset_size = 0
    
    if any(c in string.ascii_lowercase for c in password):
        charset_size += 26
    if any(c in string.ascii_uppercase for c in password):
        charset_size += 26
    if any(c in string.digits for c in password):
        charset_size += 10
    if any(c in string.punctuation for c in password):
        charset_size += 32
    
    if charset_size == 0:
        return 0
    
    entropy = len(password) * math.log2(charset_size)
    return entropy


def analyze_password(password):
    """Analyze password strength."""
    entropy = calculate_password_entropy(password)
    
    # Strength categories
    if entropy < 28:
        strength = "Very Weak"
        color = "#FF0000"
    elif entropy < 36:
        strength = "Weak"
        color = "#FF6600"
    elif entropy < 60:
        strength = "Moderate"
        color = "#FFCC00"
    elif entropy < 128:
        strength = "Strong"
        color = "#66CC00"
    else:
        strength = "Very Strong"
        color = "#00CC00"
    
    return {
        'password': password,
        'length': len(password),
        'entropy': entropy,
        'strength': strength,
        'color': color
    }


def generate_quantum_password(length=16):
    """Generate a password using quantum random numbers."""
    # Generate random bits
    bits_needed = length * 8  # 8 bits per character
    random_bits = generate_quantum_random(bits_needed)
    
    # Convert to characters
    password = []
    for i in range(length):
        # Get 8 bits for this character
        byte_bits = random_bits[i*8:(i+1)*8]
        byte_value = sum(b * (2**j) for j, b in enumerate(byte_bits))
        
        # Map to printable ASCII (32-126)
        char_value = 32 + (byte_value % 95)
        password.append(chr(char_value))
    
    return ''.join(password)


def visualize_results(analyses):
    """Create visualization."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Entropy comparison
    passwords = [a['password'][:10] + '...' if len(a['password']) > 10 
                else a['password'] for a in analyses]
    entropies = [a['entropy'] for a in analyses]
    colors = [a['color'] for a in analyses]
    
    axes[0, 0].barh(passwords, entropies, color=colors)
    axes[0, 0].set_xlabel('Entropy (bits)')
    axes[0, 0].set_title('Password Entropy')
    axes[0, 0].axvline(x=60, color='green', linestyle='--', label='Strong')
    axes[0, 0].legend()
    axes[0, 0].grid(axis='x', alpha=0.3)
    
    # Length vs Entropy
    lengths = [a['length'] for a in analyses]
    axes[0, 1].scatter(lengths, entropies, c=colors, s=100)
    axes[0, 1].set_xlabel('Password Length')
    axes[0, 1].set_ylabel('Entropy (bits)')
    axes[0, 1].set_title('Length vs Entropy')
    axes[0, 1].grid(alpha=0.3)
    
    # Strength distribution
    strengths = [a['strength'] for a in analyses]
    strength_counts = {s: strengths.count(s) for s in set(strengths)}
    axes[1, 0].pie(strength_counts.values(), labels=strength_counts.keys(),
                   autopct='%1.1f%%', colors=['#FF0000', '#FF6600', '#FFCC00', 
                                               '#66CC00', '#00CC00'][:len(strength_counts)])
    axes[1, 0].set_title('Strength Distribution')
    
    # Quantum vs Classical entropy
    quantum_entropies = [a['entropy'] for a in analyses if 'quantum' in str(a).lower()]
    classical_entropies = [a['entropy'] for a in analyses if 'quantum' not in str(a).lower()]
    
    if quantum_entropies and classical_entropies:
        axes[1, 1].bar(['Classical', 'Quantum'], 
                      [np.mean(classical_entropies), np.mean(quantum_entropies)],
                      color=['#2196F3', '#4CAF50'])
        axes[1, 1].set_ylabel('Average Entropy')
        axes[1, 1].set_title('Classical vs Quantum Entropy')
        axes[1, 1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/mike/Desktop/practic/quantum/quantum-hackthon/problem8_results.png',
                dpi=150, bbox_inches='tight')
    print("\nVisualization saved as 'problem8_results.png'")


def main():
    """Main function."""
    print("=" * 60)
    print("PROBLEM 8: QUANTUM PASSWORD STRENGTH ANALYZER")
    print("=" * 60)
    
    # Test passwords
    test_passwords = [
        "password",
        "Password123!",
        "P@ssw0rd#2024",
        "correct-horse-battery-staple",
        "Tr0ub4dor&3"
    ]
    
    analyses = []
    print("\nAnalyzing passwords:")
    for pwd in test_passwords:
        analysis = analyze_password(pwd)
        analyses.append(analysis)
        print(f"\n  '{pwd}':")
        print(f"    Length: {analysis['length']}")
        print(f"    Entropy: {analysis['entropy']:.1f} bits")
        print(f"    Strength: {analysis['strength']}")
    
    # Generate quantum password
    print("\nGenerating quantum password...")
    quantum_pwd = generate_quantum_password(16)
    quantum_analysis = analyze_password(quantum_pwd)
    analyses.append(quantum_analysis)
    
    print(f"\n  Quantum password: {quantum_pwd}")
    print(f"  Length: {quantum_analysis['length']}")
    print(f"  Entropy: {quantum_analysis['entropy']:.1f} bits")
    print(f"  Strength: {quantum_analysis['strength']}")
    
    # Visualize
    visualize_results(analyses)
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"\nPasswords analyzed: {len(analyses)}")
    print(f"Quantum password generated: {quantum_pwd}")
    print(f"Average entropy: {np.mean([a['entropy'] for a in analyses]):.1f} bits")
    print("\n✓ Problem 8 completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
