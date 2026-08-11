# Problem 6: Disaster Response Resource Allocation

## Problem Statement

During natural disasters, efficient allocation of limited resources (medical supplies, food, personnel) across affected areas is critical. This is a multi-constraint optimization problem that can benefit from quantum computing.

## Challenge

Optimize resource allocation across multiple facilities and affected areas during a disaster scenario.

## Requirements

1. **Problem Modeling**:
   - Model facilities with resource capacities
   - Model affected areas with demands
   - Define transportation costs and time constraints

2. **Optimization**:
   - Minimize response time
   - Maximize demand satisfaction
   - Respect resource constraints

3. **Multi-Objective**:
   - Balance time, cost, and coverage
   - Handle competing priorities
   - Find Pareto-optimal solutions

4. **Visualization**:
   - Resource distribution map
   - Allocation plan timeline
   - Coverage analysis

## Input

- Facility locations and capacities
- Affected area locations and demands
- Transportation network

## Output

- Resource allocation plan
- Response time analysis
- Coverage percentage
- Visualization of allocation

## Evaluation Criteria

- Quality of allocation solution
- Constraint satisfaction
- Multi-objective balancing
- Visualization effectiveness

## File

`problem6_disaster.py`
