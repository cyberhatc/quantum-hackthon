# Problem 5: Quantum ML Anomaly Detection

## Problem Statement

Cloud infrastructure generates massive log data. Detecting anomalies in real-time is crucial for maintaining system health. Quantum machine learning offers potential advantages in pattern recognition for anomaly detection.

## Challenge

Implement a quantum-enhanced anomaly detection system for cloud infrastructure metrics.

## Requirements

1. **Feature Extraction**:
   - Extract features from simulated cloud metrics
   - Normalize and prepare data for quantum processing

2. **Quantum Kernel**:
   - Implement quantum feature map
   - Calculate quantum kernel matrix
   - Compare with classical kernels

3. **Anomaly Detection**:
   - Train on normal data patterns
   - Detect deviations from normal behavior
   - Classify anomalies with confidence scores

4. **Evaluation**:
   - Compare quantum vs classical detection accuracy
   - Visualize detection results
   - Show ROC curves and metrics

## Input

- Cloud metrics time series (CPU, memory, network)
- Normal behavior patterns
- Anomalous instances for testing

## Output

- Anomaly predictions with timestamps
- Detection accuracy metrics
- Visualization of normal vs anomalous patterns
- Quantum vs classical comparison

## Evaluation Criteria

- Detection accuracy
- False positive/negative rates
- Quantum advantage demonstration
- Visualization quality

## File

`problem5_anomaly.py`
