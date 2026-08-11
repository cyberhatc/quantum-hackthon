# IBM Qiskit Fall Fest 2026 - Hackathon

## Theme: A Decade of Quantum on the Cloud

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Qiskit](https://img.shields.io/badge/Qiskit-2.5.1-6929C4?style=for-the-badge&logo=ibm-qiskit&logoColor=white)](https://qiskit.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

Solutions for all 10 hackathon problems using Qiskit and quantum computing. This repository demonstrates quantum computing applications across various domains including optimization, security, machine learning, and resource management.

---

## Table of Contents

- [Problems Overview](#problems-overview)
- [Project Structure](#project-structure)
- [Problem Statements](#problem-statements)
- [Tech Stack](#tech-stack)
- [Setup & Installation](#setup--installation)
- [Running the Solutions](#running-the-solutions)
- [Visualizations](#visualizations)
- [Author](#author)
- [License](#license)

---

## Problems Overview

| # | Problem | Folder | Difficulty | Status |
|---|---------|--------|------------|--------|
| 1 | Quantum Cloud Job Optimizer | `Quantum-Cloud-Job-Optimizer/` | Intermediate | ✅ Solved |
| 2 | Hybrid Route Optimization (QAOA) | `Hybrid-Route-Optimization/` | Intermediate | ✅ Solved |
| 3 | Quantum Secure File Sharing | `Quantum-Secure-File-Sharing/` | Intermediate | ✅ Solved |
| 4 | Green Cloud Scheduler | `Green-Cloud-Scheduler/` | Intermediate | ✅ Solved |
| 5 | Quantum ML Anomaly Detection | `Quantum-ML-Anomaly-Detection/` | Intermediate | ✅ Solved |
| 6 | Disaster Response Resource Allocation | `Disaster-Response-Resource-Allocation/` | Intermediate | ✅ Solved |
| 7 | Quantum Portfolio Optimizer | `Quantum-Portfolio-Optimizer/` | Intermediate | ✅ Solved |
| 8 | Quantum Password Strength Analyzer | `Quantum-Password-Strength-Analyzer/` | Intermediate | ✅ Solved |
| 9 | Quantum Circuit Marketplace | `Quantum-Circuit-Marketplace/` | Intermediate | ✅ Solved |
| 10 | Campus Cloud Resource Optimizer | `Campus-Cloud-Resource-Optimizer/` | Intermediate | ✅ Solved |

---

## Project Structure

```
quantum-hackthon/
│
├── README.md                          # Main project documentation
├── PROBLEMS.md                        # Detailed problem statements
├── requirements.txt                   # Python dependencies
├── quantum-hackthon.mctx              # MCTX tracking file
│
├── Quantum-Cloud-Job-Optimizer/
│   ├── problem_statement.md           # Problem statement
│   ├── solution.py                    # Solution code
│   └── results.png                    # Visualization output
│
├── Hybrid-Route-Optimization/
│   ├── problem_statement.md
│   ├── solution.py
│   └── results.png
│
├── Quantum-Secure-File-Sharing/
│   ├── problem_statement.md
│   └── solution.py
│
├── Green-Cloud-Scheduler/
│   ├── problem_statement.md
│   └── solution.py
│
├── Quantum-ML-Anomaly-Detection/
│   ├── problem_statement.md
│   └── solution.py
│
├── Disaster-Response-Resource-Allocation/
│   ├── problem_statement.md
│   └── solution.py
│
├── Quantum-Portfolio-Optimizer/
│   ├── problem_statement.md
│   ├── solution.py
│   └── results.png
│
├── Quantum-Password-Strength-Analyzer/
│   ├── problem_statement.md
│   ├── solution.py
│   └── results.png
│
├── Quantum-Circuit-Marketplace/
│   ├── problem_statement.md
│   ├── solution.py
│   └── results.png
│
└── Campus-Cloud-Resource-Optimizer/
    ├── problem_statement.md
    ├── solution.py
    └── results.png
```

---

## Problem Statements

### 1. Quantum Cloud Job Optimizer

**Challenge:** Benchmark and optimize quantum jobs across multiple cloud backends.

**Description:**
Quantum cloud computing providers offer multiple backends with varying capabilities. Developers need to select the optimal backend for their quantum circuits based on factors like execution time, queue depth, and output fidelity.

**Key Features:**
- Simulates multiple quantum backends with different noise profiles
- Benchmarks circuits for execution time, queue depth, and fidelity
- Recommends optimal backend based on performance metrics
- Generates comparative visualization charts

**Quantum Concepts Used:**
- Backend simulation
- Noise modeling
- Performance benchmarking

---

### 2. Hybrid Route Optimization (QAOA)

**Challenge:** Solve Traveling Salesman Problem using QAOA quantum optimization.

**Description:**
The Traveling Salesman Problem (TSP) is a classic optimization challenge. This solution implements a hybrid quantum-classical approach using QAOA (Quantum Approximate Optimization Algorithm) for route optimization.

**Key Features:**
- QAOA-based route optimization
- Hybrid quantum-classical optimization loop
- Multiple cities with distance matrices
- Route visualization on 2D plane

**Quantum Concepts Used:**
- QAOA algorithm
- Parameterized quantum circuits
- Classical-quantum optimization loop

---

### 3. Quantum Secure File Sharing

**Challenge:** Implement quantum-secure file sharing using QRNG and QKD.

**Description:**
Classical encryption methods face threats from quantum computers. This solution uses Quantum Random Number Generation (QRNG) and Quantum Key Distribution (QKD) for information-theoretically secure file sharing.

**Key Features:**
- QRNG for truly random key generation
- BB84-style QKD protocol simulation
- XOR encryption with quantum-generated keys
- Eavesdropping detection demonstration

**Quantum Concepts Used:**
- Quantum random number generation
- Quantum key distribution
- BB84 protocol

---

### 4. Green Cloud Scheduler

**Challenge:** Optimize datacenter energy consumption using quantum optimization.

**Description:**
Datacenters consume massive amounts of energy. This solution optimizes workload scheduling to align with renewable energy availability, reducing carbon footprint while maintaining performance SLAs.

**Key Features:**
- Workload scheduling with energy constraints
- Renewable energy utilization optimization
- Carbon footprint minimization
- Energy vs performance tradeoff analysis

**Quantum Concepts Used:**
- Quantum-inspired optimization
- Multi-constraint optimization
- Resource scheduling

---

### 5. Quantum ML Anomaly Detection

**Challenge:** Detect cloud infrastructure anomalies using quantum machine learning.

**Description:**
Cloud infrastructure generates massive log data. This solution uses quantum machine learning for anomaly detection, leveraging quantum kernels for feature extraction and pattern recognition.

**Key Features:**
- Quantum kernel for feature extraction
- Anomaly detection in cloud metrics
- Quantum vs classical comparison
- Detection accuracy visualization

**Quantum Concepts Used:**
- Quantum feature maps
- Quantum kernel methods
- Quantum machine learning

---

### 6. Disaster Response Resource Allocation

**Challenge:** Optimize resource allocation during disasters using quantum computing.

**Description:**
During natural disasters, efficient allocation of limited resources across affected areas is critical. This solution implements multi-constraint optimization for disaster response resource allocation.

**Key Features:**
- Multi-resource type optimization
- Time, distance, and demand constraints
- Multiple facilities and affected areas
- Resource distribution visualization

**Quantum Concepts Used:**
- Multi-constraint optimization
- Quantum-inspired algorithms
- Facility location optimization

---

### 7. Quantum Portfolio Optimizer

**Challenge:** Optimize cloud service allocation using portfolio theory and quantum optimization.

**Description:**
Cloud service providers offer multiple services with varying costs, benefits, and risks. This solution applies portfolio optimization theory to find the optimal balance of cost, benefit, and risk.

**Key Features:**
- Cost, benefit, and risk modeling
- Budget constraint optimization
- Efficient frontier calculation
- Quantum vs classical comparison

**Quantum Concepts Used:**
- Portfolio optimization
- Quantum-inspired optimization
- Risk-return analysis

---

### 8. Quantum Password Strength Analyzer

**Challenge:** Analyze password strength using quantum random number generation.

**Description:**
Password security relies on randomness. This solution uses QRNG for truly random password generation and provides entropy-based strength classification.

**Key Features:**
- QRNG-based password generation
- Entropy calculation and strength classification
- Quantum vs classical comparison
- Strength distribution visualization

**Quantum Concepts Used:**
- Quantum random number generation
- Entropy calculation
- Password strength analysis

---

### 9. Quantum Circuit Marketplace

**Challenge:** Create a cloud platform for sharing, benchmarking, and comparing quantum circuits.

**Description:**
As quantum computing grows, developers need to share and compare quantum circuits. This solution implements a circuit marketplace with benchmarking capabilities.

**Key Features:**
- Circuit library (Bell state, GHZ, QFT, Grover's)
- Performance benchmarking
- Circuit comparison metrics
- Marketplace visualization

**Quantum Concepts Used:**
- Circuit analysis
- Performance benchmarking
- Quantum circuit comparison

---

### 10. Campus Cloud Resource Optimizer

**Challenge:** Optimize campus lab booking and GPU allocation using quantum optimization.

**Description:**
Universities have limited computing resources. This solution implements a resource allocation system using quantum-inspired optimization to maximize utilization while respecting priorities.

**Key Features:**
- Lab booking system
- Priority-based allocation
- Resource utilization optimization
- Quantum vs classical comparison

**Quantum Concepts Used:**
- Resource optimization
- Priority-based scheduling
- Quantum-inspired algorithms

---

## Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.14 | Core programming language |
| Qiskit | 2.5.1 | Quantum computing framework |
| Qiskit IBM Runtime | 0.49.0 | IBM Quantum Platform integration |
| Qiskit Aer | 0.17.2 | Quantum circuit simulation |
| NumPy | Latest | Numerical computing |
| Matplotlib | Latest | Data visualization |

---

## Setup & Installation

### Prerequisites

- Python 3.14 or higher
- pip package manager
- Git

### Installation Steps

```bash
# Clone the repository
git clone https://github.com/cyberhatc/quantum-hackthon.git
cd quantum-hackthon

# Activate virtual environment
source /home/mike/Desktop/practic/env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Dependencies

```
qiskit==2.5.1
qiskit-ibm-runtime==0.49.0
qiskit-aer==0.17.2
numpy
matplotlib
```

---

## Running the Solutions

### Running Individual Problems

```bash
# Problem 1: Quantum Cloud Job Optimizer
python Quantum-Cloud-Job-Optimizer/solution.py

# Problem 2: Hybrid Route Optimization
python Hybrid-Route-Optimization/solution.py

# Problem 3: Quantum Secure File Sharing
python Quantum-Secure-File-Sharing/solution.py

# Problem 4: Green Cloud Scheduler
python Green-Cloud-Scheduler/solution.py

# Problem 5: Quantum ML Anomaly Detection
python Quantum-ML-Anomaly-Detection/solution.py

# Problem 6: Disaster Response Resource Allocation
python Disaster-Response-Resource-Allocation/solution.py

# Problem 7: Quantum Portfolio Optimizer
python Quantum-Portfolio-Optimizer/solution.py

# Problem 8: Quantum Password Strength Analyzer
python Quantum-Password-Strength-Analyzer/solution.py

# Problem 9: Quantum Circuit Marketplace
python Quantum-Circuit-Marketplace/solution.py

# Problem 10: Campus Cloud Resource Optimizer
python Campus-Cloud-Resource-Optimizer/solution.py
```

### Expected Output

Each solution will:
1. Print problem description and results to console
2. Generate visualization plots (saved as `results.png`)
3. Display performance metrics and comparisons

---

## Visualizations

Each problem generates visualization plots saved as `results.png` in their respective folders:

| Problem | Visualization |
|---------|---------------|
| 1 | Backend performance comparison charts |
| 2 | Route optimization visualization |
| 4 | Energy consumption timeline |
| 5 | Anomaly detection results |
| 6 | Resource allocation map |
| 7 | Efficient frontier plot |
| 8 | Password strength distribution |
| 9 | Circuit comparison metrics |
| 10 | Resource utilization charts |

---

## GitHub Issues

- [Issue #11](https://github.com/cyberhatc/quantum-hackthon/issues/11) - File organization fix (completed)

---

## Author

**mike** - student/quantum-developer

- GitHub: [cyberhatc](https://github.com/cyberhatc)
- Repository: [quantum-hackthon](https://github.com/cyberhatc/quantum-hackthon)

---

## Acknowledgments

- IBM for organizing Qiskit Fall Fest 2026
- Qiskit community for excellent documentation and support
- Quantum computing researchers for advancing the field

---

## License

This project is part of IBM Qiskit Fall Fest 2026 Hackathon.

MIT License - see [LICENSE](LICENSE) for details.
