# Problem 8: Quantum Password Strength Analyzer

## Problem Statement

Password security relies on randomness. Quantum Random Number Generation (QRNG) provides truly random numbers, enabling stronger password generation and more accurate entropy calculation.

## Challenge

Implement a password strength analyzer using quantum random numbers for generation and entropy-based strength classification.

## Requirements

1. **QRNG Implementation**:
   - Generate truly random bits using quantum measurement
   - Convert random bits to password characters

2. **Entropy Calculation**:
   - Calculate password entropy based on character set
   - Classify strength (Very Weak to Very Strong)

3. **Password Generation**:
   - Generate passwords using quantum randomness
   - Configurable length and character sets

4. **Comparison**:
   - Compare quantum vs classical passwords
   - Show entropy distribution
   - Visualize strength categories

## Input

- Passwords to analyze (user-provided or generated)
- Generation parameters (length, character set)

## Output

- Password strength analysis
- Entropy calculations
- Quantum password generation
- Strength distribution visualization

## Evaluation Criteria

- QRNG correctness
- Entropy calculation accuracy
- Password strength classification
- Visualization quality

## File

`problem8_password.py`
