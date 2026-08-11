# Problem 10: Campus Cloud Resource Optimizer

## Problem Statement

Universities have limited computing resources (labs, GPUs, CPUs). Optimizing resource allocation across research projects, courses, and priorities is a complex scheduling problem.

## Challenge

Implement a resource allocation system for campus computing resources using quantum-inspired optimization.

## Requirements

1. **Resource Modeling**:
   - Model labs with different capabilities (GPU, CPU, memory)
   - Model time slots for booking
   - Track resource availability

2. **Request Handling**:
   - Accept booking requests with requirements
   - Handle priority levels
   - Manage conflicts

3. **Optimization**:
   - Maximize resource utilization
   - Respect priority constraints
   - Minimize booking conflicts

4. **Comparison**:
   - Compare quantum vs greedy allocation
   - Show utilization improvements
   - Analyze booking success rates

## Input

- Lab configurations (capacity, capabilities)
- Booking requests (requirements, priority)
- Time slot definitions

## Output

- Allocation plan
- Utilization statistics
- Booking success rate
- Quantum vs greedy comparison

## Evaluation Criteria

- Allocation quality
- Utilization improvement
- Priority handling
- Visualization clarity

## File

`problem10_campus.py`
