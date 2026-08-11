#!/usr/bin/env python3
"""
Problem 3: Quantum Secure File Sharing
=======================================

Prototype encrypted cloud file sharing using post-quantum cryptography
with a quantum random number generator simulation.
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import hashlib


def generate_quantum_random_bits(num_bits):
    """Generate random bits using quantum measurement."""
    print(f"Generating {num_bits} random bits using quantum circuit...")
    
    qc = QuantumCircuit(num_bits, num_bits)
    qc.h(range(num_bits))  # Hadamard creates superposition
    qc.measure(range(num_bits), range(num_bits))
    
    simulator = AerSimulator()
    job = simulator.run(qc, shots=1)
    result = job.result()
    counts = result.get_counts(qc)
    
    # Extract bits
    bitstring = list(counts.keys())[0]
    bits = [int(b) for b in bitstring[::-1]]
    
    return bits


def quantum_key_distribution(bits):
    """Simulate BB84-like key distribution."""
    print("Running QKD simulation...")
    
    num_bits = len(bits)
    
    # Alice's bases (random)
    alice_bases = np.random.randint(0, 2, num_bits)
    
    # Bob's bases (random)
    bob_bases = np.random.randint(0, 2, num_bits)
    
    # Keep bits where bases match
    matching = alice_bases == bob_bases
    key = [bits[i] for i in range(num_bits) if matching[i]]
    
    print(f"  Original bits: {num_bits}")
    print(f"  Matching bases: {sum(matching)}")
    print(f"  Final key length: {len(key)}")
    
    return key


def xor_encrypt(data, key):
    """Encrypt data using XOR with key."""
    encrypted = []
    for i, byte in enumerate(data):
        key_byte = key[i % len(key)]
        encrypted.append(byte ^ key_byte)
    return encrypted


def xor_decrypt(data, key):
    """Decrypt data using XOR with key."""
    return xor_encrypt(data, key)  # XOR is its own inverse


def visualize_key_distribution(key):
    """Visualize the generated key."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Key bit distribution
    zeros = key.count(0)
    ones = key.count(1)
    axes[0].bar(['0', '1'], [zeros, ones], color=['#2196F3', '#FF5722'])
    axes[0].set_title('Quantum Key Distribution')
    axes[0].set_ylabel('Count')
    axes[0].grid(axis='y', alpha=0.3)
    
    # Key entropy
    p0 = zeros / len(key) if len(key) > 0 else 0
    p1 = ones / len(key) if len(key) > 0 else 0
    entropy = -sum(p * np.log2(p) for p in [p0, p1] if p > 0)
    
    axes[1].bar(['Entropy'], [entropy], color='#4CAF50')
    axes[1].axhline(y=1.0, color='red', linestyle='--', label='Max entropy')
    axes[1].set_title(f'Key Entropy: {entropy:.3f} bits')
    axes[1].set_ylim(0, 1.2)
    axes[1].legend()
    axes[1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/mike/Desktop/practic/quantum/quantum-hackthon/problem3_results.png',
                dpi=150, bbox_inches='tight')
    print("\nVisualization saved as 'problem3_results.png'")


def main():
    """Main function."""
    print("=" * 60)
    print("PROBLEM 3: QUANTUM SECURE FILE SHARING")
    print("=" * 60)
    
    # Generate quantum random key
    num_key_bits = 64
    raw_bits = generate_quantum_random_bits(num_key_bits)
    
    # QKD to get shared key
    shared_key = quantum_key_distribution(raw_bits)
    
    print(f"\nShared key: {''.join(map(str, shared_key[:16]))}...")
    
    # Test encryption
    message = "Hello, Quantum World!"
    message_bytes = list(message.encode())
    
    print(f"\nOriginal message: {message}")
    
    # Encrypt
    encrypted = xor_encrypt(message_bytes, shared_key)
    print(f"Encrypted: {encrypted[:16]}...")
    
    # Decrypt
    decrypted = xor_decrypt(encrypted, shared_key)
    decrypted_message = bytes(decrypted).decode()
    print(f"Decrypted: {decrypted_message}")
    
    # Verify
    success = message == decrypted_message
    print(f"\nEncryption {'successful' if success else 'failed'}!")
    
    # Visualize
    visualize_key_distribution(shared_key)
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"\nKey length: {len(shared_key)} bits")
    print(f"Message encrypted: {message}")
    print(f"Decryption verified: {success}")
    print("\n✓ Problem 3 completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
