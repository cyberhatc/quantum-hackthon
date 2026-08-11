# IBM Qiskit Fall Fest 2026 - Hackathon Problems

## Theme: A Decade of Quantum on the Cloud

---

## Problem 1: Quantum Cloud Job Optimizer
**File:** `problem1_optimizer.py`

### Problem Statement
Quantum cloud computing providers offer multiple backends with varying capabilities. Developers need to select the optimal backend for their quantum circuits based on factors like execution time, queue depth, and output fidelity.

### Requirements
- Benchmark quantum circuits across multiple simulated cloud backends
- Compare execution times, queue depths, and output fidelities
- Recommend the optimal backend for given circuit types
- Visualize benchmark results with comparative charts

### Solution
Uses Qiskit Aer to simulate multiple backends with different noise profiles, benchmarks circuits, and recommends the best backend based on performance metrics.

---

## Problem 2: Hybrid Route Optimization (QAOA)
**File:** `problem2_routing.py`

### Problem Statement
The Traveling Salesman Problem (TSP) is a classic optimization challenge. While classical algorithms can solve small instances, quantum approaches using QAOA (Quantum Approximate Optimization Algorithm) offer potential advantages for larger problem sizes.

### Requirements
- Implement QAOA-based route optimization for TSP
- Create a hybrid quantum-classical optimization loop
- Handle multiple cities with distance matrices
- Visualize the optimal route on a map

### Solution
Implements a simplified QAOA approach using Qiskit, with classical pre-processing for distance calculations and quantum optimization for route selection.

---

## Problem 3: Quantum Secure File Sharing (QRNG + QKD)
**File:** `problem3_security.py`

### Problem Statement
Classical encryption methods face threats from quantum computers. Quantum Key Distribution (QKD) and Quantum Random Number Generation (QRNG) provide information-theoretically secure alternatives for file sharing.

### Requirements
- Implement QRNG for generating truly random encryption keys
- Simulate QKD protocol for secure key exchange
- Encrypt/decrypt files using quantum-generated keys
- Demonstrate quantum advantage in key randomness

### Solution
Uses Qiskit to generate quantum random numbers, simulates BB84-style QKD protocol, and implements XOR encryption with quantum-generated keys.

---

## Problem 4: Green Cloud Scheduler
**File:** `problem4_green.py`

### Problem Statement
Datacenters consume massive amounts of energy. Scheduling workloads to align with renewable energy availability can significantly reduce carbon footprint while maintaining performance SLAs.

### Requirements
- Model workload scheduling with energy constraints
- Optimize for renewable energy utilization
- Minimize carbon footprint while meeting deadlines
- Compare energy-optimized vs performance-optimized scheduling

### Solution
Implements a quantum-inspired optimization for workload scheduling, balancing energy consumption, carbon footprint, and execution deadlines.

---

## Problem 5: Quantum ML Anomaly Detection
**File:** `problem5_anomaly.py`

### Problem Statement
Cloud infrastructure generates massive log data. Detecting anomalies in real-time is crucial for maintaining system health. Quantum machine learning offers potential advantages in pattern recognition for anomaly detection.

### Requirements
- Implement quantum kernel for feature extraction
- Detect anomalies in simulated cloud metrics
- Compare quantum vs classical detection accuracy
- Visualize detection results with highlighting

### Solution
Uses quantum feature maps and kernel methods to detect anomalies in cloud infrastructure metrics, demonstrating quantum advantage in pattern recognition.

---

## Problem 6: Disaster Response Resource Allocation
**File:** `problem6_disaster.py`

### Problem Statement
During natural disasters, efficient allocation of limited resources (medical supplies, food, personnel) across affected areas is critical. This is a multi-constraint optimization problem that can benefit from quantum computing.

### Requirements
- Model disaster response with multiple resource types
- Optimize allocation considering time, distance, and demand
- Handle multiple facilities and affected areas
- Visualize allocation plan with resource distribution

### Solution
Implements a multi-constraint optimization for disaster response, using quantum-inspired algorithms to find optimal resource allocation.

---

## Problem 7: Quantum Portfolio Optimizer
**File:** `problem7_portfolio.py`

### Problem Statement
Cloud service providers offer multiple services with varying costs, benefits, and risks. Optimizing service allocation under budget constraints is analogous to financial portfolio optimization.

### Requirements
- Model cloud services with cost, benefit, and risk metrics
- Optimize allocation under budget constraints
- Calculate efficient frontier of risk vs return
- Compare quantum vs classical optimization

### Solution
Applies portfolio optimization theory to cloud service allocation, using quantum-inspired optimization to find the optimal balance of cost, benefit, and risk.

---

## Problem 8: Quantum Password Strength Analyzer
**File:** `problem8_password.py`

### Problem Statement
Password security relies on randomness. Quantum Random Number Generation (QRNG) provides truly random numbers, enabling stronger password generation and more accurate entropy calculation.

### Requirements
- Analyze password strength using entropy calculations
- Generate passwords using quantum random numbers
- Compare quantum vs classical password strength
- Visualize entropy distribution and strength categories

### Solution
Uses Qiskit to generate quantum random numbers for password generation, calculates entropy based on character set size, and classifies password strength.

---

## Problem 9: Quantum Circuit Marketplace
**File:** `problem9_marketplace.py`

### Problem Statement
As quantum computing grows, developers need to share, benchmark, and compare quantum circuits. A marketplace platform enables circuit discovery, performance comparison, and reuse.

### Requirements
- Create a library of quantum circuits (Bell state, GHZ, QFT, Grover's)
- Benchmark circuits for execution time and output distribution
- Compare circuit performance metrics
- Visualize circuit comparisons

### Solution
Implements a circuit marketplace with benchmarking capabilities, comparing circuits based on qubit count, gate count, execution time, and output entropy.

---

## Problem 10: Campus Cloud Resource Optimizer
**File:** `problem10_campus.py`

### Problem Statement
Universities have limited computing resources (labs, GPUs, CPUs). Optimizing resource allocation across research projects, courses, and priorities is a complex scheduling problem.

### Requirements
- Model campus resources (labs, time slots, capacities)
- Handle multiple booking requests with priorities
- Optimize utilization across all resources
- Compare quantum vs classical allocation strategies

### Solution
Implements a resource allocation system for campus computing, using quantum-inspired optimization to maximize resource utilization while respecting priorities.

---

## Tech Stack
- Python 3.14
- Qiskit 2.5.1
- Qiskit IBM Runtime 0.49.0
- Qiskit Aer 0.17.2
- NumPy
- Matplotlib

## Running the Solutions
```bash
source /home/mike/Desktop/practic/env/bin/activate
python problem1_optimizer.py
python problem2_routing.py
# ... etc
```
