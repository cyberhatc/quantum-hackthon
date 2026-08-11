# Problem 4: Green Cloud Scheduler

## Problem Statement

Datacenters consume massive amounts of energy. Scheduling workloads to align with renewable energy availability can significantly reduce carbon footprint while maintaining performance SLAs.

## Challenge

Optimize workload scheduling across datacenters to minimize carbon footprint while meeting execution deadlines.

## Requirements

1. **Energy Modeling**:
   - Model workload energy consumption
   - Track renewable energy availability (solar, wind)
   - Calculate carbon intensity by time of day

2. **Scheduling Optimization**:
   - Assign workloads to time slots
   - Respect deadline constraints
   - Maximize renewable energy usage

3. **Trade-off Analysis**:
   - Compare energy-optimized vs performance-optimized
   - Show carbon footprint reduction
   - Demonstrate SLA compliance

4. **Visualization**:
   - Energy consumption timeline
   - Renewable energy utilization
   - Carbon footprint comparison

## Input

- List of workloads with deadlines and energy requirements
- Renewable energy availability schedule
- Carbon intensity data

## Output

- Optimized schedule
- Carbon footprint reduction percentage
- Energy utilization charts
- SLA compliance report

## Evaluation Criteria

- Quality of optimization algorithm
- Carbon footprint reduction achieved
- SLA compliance maintenance
- Visualization clarity

## File

`problem4_green.py`
