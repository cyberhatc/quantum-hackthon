# Problem 3: Quantum Secure File Sharing

## Problem Statement

Classical encryption methods face threats from quantum computers. Quantum Key Distribution (QKD) and Quantum Random Number Generation (QRNG) provide information-theoretically secure alternatives for file sharing.

## Challenge

Implement a quantum-secure file sharing system using QRNG for key generation and QKD for secure key exchange.

## Requirements

1. **QRNG Implementation**:
   - Generate truly random bits using quantum measurement
   - Achieve uniform distribution of 0s and 1s

2. **QKD Protocol**:
   - Simulate BB84-style key exchange
   - Detect eavesdropping attempts
   - Establish shared secret key

3. **Encryption**:
   - XOR encryption with quantum-generated keys
   - File encryption/decryption
   - Key management

4. **Security Demonstration**:
   - Show quantum randomness vs classical pseudo-randomness
   - Demonstrate eavesdropping detection

## Input

- File to encrypt (text or binary)
- Quantum channel for key exchange

## Output

- Encrypted file
- Decrypted file (verified match)
- Key statistics
- Security analysis

## Evaluation Criteria

- Correctness of QRNG implementation
- QKD protocol fidelity
- Encryption/decryption accuracy
- Security demonstration effectiveness

## File

`problem3_security.py`
