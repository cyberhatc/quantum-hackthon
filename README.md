# IBM Qiskit Fall Fest 2026 - Hackathon

## Theme: A Decade of Quantum on the Cloud

Solutions for all 10 hackathon problems using Qiskit and quantum computing.

---

## Problems Overview

| # | Problem | Folder | Status |
|---|---------|--------|--------|
| 1 | Quantum Cloud Job Optimizer | `problems/problem1/` | ✅ |
| 2 | Hybrid Route Optimization (QAOA) | `problems/problem2/` | ✅ |
| 3 | Quantum Secure File Sharing | `problems/problem3/` | ✅ |
| 4 | Green Cloud Scheduler | `problems/problem4/` | ✅ |
| 5 | Quantum ML Anomaly Detection | `problems/problem5/` | ✅ |
| 6 | Disaster Response Resource Allocation | `problems/problem6/` | ✅ |
| 7 | Quantum Portfolio Optimizer | `problems/problem7/` | ✅ |
| 8 | Quantum Password Strength Analyzer | `problems/problem8/` | ✅ |
| 9 | Quantum Circuit Marketplace | `problems/problem9/` | ✅ |
| 10 | Campus Cloud Resource Optimizer | `problems/problem10/` | ✅ |

---

## Problem Statements

### Problem 1: Quantum Cloud Job Optimizer

**Challenge:** Benchmark and optimize quantum jobs across multiple cloud backends.

**Requirements:**
- Compare execution times, queue depths, and fidelities across backends
- Recommend optimal backend for given circuit types
- Visualize benchmark results with comparative charts

**Solution:** Uses Qiskit Aer to simulate multiple backends with different noise profiles, benchmarks circuits, and recommends the best backend based on performance metrics.

---

### Problem 2: Hybrid Route Optimization (QAOA)

**Challenge:** Solve Traveling Salesman Problem using QAOA quantum optimization.

**Requirements:**
- Implement QAOA-based route optimization for TSP
- Create hybrid quantum-classical optimization loop
- Handle multiple cities with distance matrices
- Visualize optimal route on a map

**Solution:** Implements a simplified QAOA approach using Qiskit, with classical pre-processing for distance calculations and quantum optimization for route selection.

---

### Problem 3: Quantum Secure File Sharing

**Challenge:** Implement quantum-secure file sharing using QRNG and QKD.

**Requirements:**
- Quantum Random Number Generator for truly random keys
- Simulate QKD protocol for secure key exchange
- XOR encryption with quantum-generated keys
- Demonstrate quantum advantage in key randomness

**Solution:** Uses Qiskit to generate quantum random numbers, simulates BB84-style QKD protocol, and implements XOR encryption with quantum-generated keys.

---

### Problem 4: Green Cloud Scheduler

**Challenge:** Optimize datacenter energy consumption using quantum optimization.

**Requirements:**
- Model workload scheduling with energy constraints
- Optimize for renewable energy utilization
- Minimize carbon footprint while meeting deadlines
- Compare energy-optimized vs performance-optimized scheduling

**Solution:** Implements a quantum-inspired optimization for workload scheduling, balancing energy consumption, carbon footprint, and execution deadlines.

---

### Problem 5: Quantum ML Anomaly Detection

**Challenge:** Detect cloud infrastructure anomalies using quantum machine learning.

**Requirements:**
- Implement quantum kernel for feature extraction
- Detect anomalies in simulated cloud metrics
- Compare quantum vs classical detection accuracy
- Visualize detection results with highlighting

**Solution:** Uses quantum feature maps and kernel methods to detect anomalies in cloud infrastructure metrics, demonstrating quantum advantage in pattern recognition.

---

### Problem 6: Disaster Response Resource Allocation

**Challenge:** Optimize resource allocation during disasters using quantum computing.

**Requirements:**
- Model disaster response with multiple resource types
- Optimize allocation considering time, distance, and demand
- Handle multiple facilities and affected areas
- Visualize allocation plan with resource distribution

**Solution:** Implements a multi-constraint optimization for disaster response, using quantum-inspired algorithms to find optimal resource allocation.

---

### Problem 7: Quantum Portfolio Optimizer

**Challenge:** Optimize cloud service allocation using portfolio theory and quantum optimization.

**Requirements:**
- Model cloud services with cost, benefit, and risk metrics
- Optimize allocation under budget constraints
- Calculate efficient frontier of risk vs return
- Compare quantum vs classical optimization

**Solution:** Applies portfolio optimization theory to cloud service allocation, using quantum-inspired optimization to find the optimal balance of cost, benefit, and risk.

---

### Problem 8: Quantum Password Strength Analyzer

**Challenge:** Analyze password strength using quantum random number generation.

**Requirements:**
- QRNG-based password generation
- Entropy calculation and strength classification
- Quantum vs classical password comparison
- Visualize entropy distribution and strength categories

**Solution:** Uses Qiskit to generate quantum random numbers for password generation, calculates entropy based on character set size, and classifies password strength.

---

### Problem 9: Quantum Circuit Marketplace

**Challenge:** Create a cloud platform for sharing, benchmarking, and comparing quantum circuits.

**Requirements:**
- Circuit library (Bell state, GHZ, QFT, Grover's)
- Benchmark circuits for execution time and output distribution
- Compare circuit performance metrics
- Visualize circuit comparisons

**Solution:** Implements a circuit marketplace with benchmarking capabilities, comparing circuits based on qubit count, gate count, execution time, and output entropy.

---

### Problem 10: Campus Cloud Resource Optimizer

**Challenge:** Optimize campus lab booking and GPU allocation using quantum optimization.

**Requirements:**
- Model campus resources (labs, time slots, capacities)
- Handle multiple booking requests with priorities
- Optimize utilization across all resources
- Compare quantum vs classical allocation strategies

**Solution:** Implements a resource allocation system for campus computing, using quantum-inspired optimization to maximize resource utilization while respecting priorities.

---

## Project Structure

```
quantum-hackthon/
├── README.md                    # This file
├── PROBLEMS.md                  # Detailed problem statements
├── requirements.txt             # Python dependencies
├── quantum-hackthon.mctx        # MCTX tracking file
└── problems/
    ├── problem1/
    │   ├── README.md            # Problem 1 statement
    │   └── solution.py          # Problem 1 solution
    ├── problem2/
    │   ├── README.md            # Problem 2 statement
    │   └── solution.py          # Problem 2 solution
    ├── problem3/
    │   ├── README.md            # Problem 3 statement
    │   └── solution.py          # Problem 3 solution
    ├── problem4/
    │   ├── README.md            # Problem 4 statement
    │   └── solution.py          # Problem 4 solution
    ├── problem5/
    │   ├── README.md            # Problem 5 statement
    │   └── solution.py          # Problem 5 solution
    ├── problem6/
    │   ├── README.md            # Problem 6 statement
    │   └── solution.py          # Problem 6 solution
    ├── problem7/
    │   ├── README.md            # Problem 7 statement
    │   └── solution.py          # Problem 7 solution
    ├── problem8/
    │   ├── README.md            # Problem 8 statement
    │   └── solution.py          # Problem 8 solution
    ├── problem9/
    │   ├── README.md            # Problem 9 statement
    │   └── solution.py          # Problem 9 solution
    └── problem10/
        ├── README.md            # Problem 10 statement
        └── solution.py          # Problem 10 solution
```

---

## Running the Solutions

### Prerequisites

- Python 3.14
- Qiskit 2.5.1
- Qiskit IBM Runtime 0.49.0
- Qiskit Aer 0.17.2
- NumPy
- Matplotlib

### Setup

```bash
# Activate virtual environment
source /home/mike/Desktop/practic/env/bin/activate

# Install dependencies (if needed)
pip install -r requirements.txt
```

### Running Individual Problems

```bash
# Problem 1: Quantum Cloud Job Optimizer
python problems/problem1/solution.py

# Problem 2: Hybrid Route Optimization
python problems/problem2/solution.py

# Problem 3: Quantum Secure File Sharing
python problems/problem3/solution.py

# Problem 4: Green Cloud Scheduler
python problems/problem4/solution.py

# Problem 5: Quantum ML Anomaly Detection
python problems/problem5/solution.py

# Problem 6: Disaster Response Resource Allocation
python problems/problem6/solution.py

# Problem 7: Quantum Portfolio Optimizer
python problems/problem7/solution.py

# Problem 8: Quantum Password Strength Analyzer
python problems/problem8/solution.py

# Problem 9: Quantum Circuit Marketplace
python problems/problem9/solution.py

# Problem 10: Campus Cloud Resource Optimizer
python problems/problem10/solution.py
```

---

## Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.14 | Core language |
| Qiskit | 2.5.1 | Quantum computing framework |
| Qiskit IBM Runtime | 0.49.0 | IBM Quantum Platform integration |
| Qiskit Aer | 0.17.2 | Quantum simulation |
| NumPy | - | Numerical computing |
| Matplotlib | - | Data visualization |

---

## GitHub Issues

- [Issue #11](https://github.com/cyberhatc/quantum-hackthon/issues/11) - Fix file organization (this fix)

---

## Author

**mike** - student/quantum-developer

---

## License

This project is part of IBM Qiskit Fall Fest 2026 Hackathon.
