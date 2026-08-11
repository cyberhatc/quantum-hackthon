#!/usr/bin/env python3
"""
Problem 5: Quantum ML for Cloud Anomaly Detection
==================================================

Detect anomalies in cloud/server metrics using quantum kernels
or variational classifiers.
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def generate_cloud_metrics(num_samples=100):
    """Generate simulated cloud metrics."""
    np.random.seed(42)
    
    metrics = []
    labels = []
    
    for _ in range(num_samples):
        if np.random.random() < 0.1:  # 10% anomalies
            # Anomalous metrics
            cpu = np.random.uniform(80, 100)
            memory = np.random.uniform(85, 100)
            requests = np.random.uniform(10000, 50000)
            errors = np.random.uniform(50, 200)
            label = 1  # Anomaly
        else:
            # Normal metrics
            cpu = np.random.uniform(10, 60)
            memory = np.random.uniform(30, 70)
            requests = np.random.uniform(100, 5000)
            errors = np.random.uniform(0, 20)
            label = 0  # Normal
        
        metrics.append([cpu, memory, requests, errors])
        labels.append(label)
    
    return np.array(metrics), np.array(labels)


def normalize_metrics(metrics):
    """Normalize metrics to [0, 1] range."""
    min_vals = metrics.min(axis=0)
    max_vals = metrics.max(axis=0)
    return (metrics - min_vals) / (max_vals - min_vals + 1e-8)


def quantum_kernel(x1, x2):
    """Compute quantum kernel between two feature vectors."""
    # Create quantum circuit for kernel computation
    qc = QuantumCircuit(2)
    
    # Encode first vector
    qc.ry(x1[0] * np.pi, 0)
    qc.ry(x1[1] * np.pi, 1)
    
    # Entangle
    qc.cx(0, 1)
    
    # Encode second vector (inverse)
    qc.ry(-x2[0] * np.pi, 0)
    qc.ry(-x2[1] * np.pi, 1)
    
    # Measure
    sv = Statevector.from_instruction(qc)
    probs = sv.probabilities_dict()
    
    # Kernel value is probability of |00⟩
    return probs.get('00', 0)


def quantum_anomaly_detector(metrics, labels, test_point):
    """Detect anomaly using quantum kernel."""
    # Normalize
    all_data = np.vstack([metrics, test_point.reshape(1, -1)])
    normalized = normalize_metrics(all_data)
    
    # Compute kernels
    kernels = []
    for i in range(len(metrics)):
        k = quantum_kernel(normalized[i], normalized[-1])
        kernels.append(k)
    
    # Weighted average of labels
    weights = np.array(kernels)
    weights = weights / weights.sum()
    
    prediction = np.sum(weights * labels)
    
    return prediction, kernels


def visualize_results(metrics, labels, predictions):
    """Create visualization."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Scatter plot of metrics
    normal = metrics[labels == 0]
    anomaly = metrics[labels == 1]
    
    axes[0, 0].scatter(normal[:, 0], normal[:, 1], c='blue', label='Normal', alpha=0.6)
    axes[0, 0].scatter(anomaly[:, 0], anomaly[:, 1], c='red', label='Anomaly', alpha=0.6)
    axes[0, 0].set_xlabel('CPU Usage')
    axes[0, 0].set_ylabel('Memory Usage')
    axes[0, 0].set_title('Cloud Metrics Distribution')
    axes[0, 0].legend()
    axes[0, 0].grid(alpha=0.3)
    
    # Prediction distribution
    axes[0, 1].hist(predictions, bins=20, color='#2196F3', edgecolor='black')
    axes[0, 1].axvline(x=0.5, color='red', linestyle='--', label='Threshold')
    axes[0, 1].set_xlabel('Anomaly Score')
    axes[0, 1].set_ylabel('Count')
    axes[0, 1].set_title('Anomaly Score Distribution')
    axes[0, 1].legend()
    axes[0, 1].grid(axis='y', alpha=0.3)
    
    # Detection results
    detected = predictions > 0.5
    correct = detected == labels
    accuracy = correct.mean() * 100
    
    tp = ((detected == 1) & (labels == 1)).sum()
    fp = ((detected == 1) & (labels == 0)).sum()
    tn = ((detected == 0) & (labels == 0)).sum()
    fn = ((detected == 0) & (labels == 1)).sum()
    
    confusion = np.array([[tn, fp], [fn, tp]])
    im = axes[1, 0].imshow(confusion, cmap='Blues')
    axes[1, 0].set_xticks([0, 1])
    axes[1, 0].set_yticks([0, 1])
    axes[1, 0].set_xticklabels(['Normal', 'Anomaly'])
    axes[1, 0].set_yticklabels(['Normal', 'Anomaly'])
    axes[1, 0].set_xlabel('Predicted')
    axes[1, 0].set_ylabel('Actual')
    axes[1, 0].set_title(f'Confusion Matrix (Accuracy: {accuracy:.1f}%)')
    
    for i in range(2):
        for j in range(2):
            axes[1, 0].text(j, i, str(confusion[i, j]), ha='center', va='center')
    
    # Metrics summary
    metrics_data = {
        'Accuracy': accuracy,
        'Precision': tp / (tp + fp) * 100 if (tp + fp) > 0 else 0,
        'Recall': tp / (tp + fn) * 100 if (tp + fn) > 0 else 0
    }
    
    axes[1, 1].bar(metrics_data.keys(), metrics_data.values(), color=['#2196F3', '#4CAF50', '#FF9800'])
    axes[1, 1].set_ylabel('Score (%)')
    axes[1, 1].set_title('Detection Metrics')
    axes[1, 1].set_ylim(0, 100)
    axes[1, 1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/mike/Desktop/practic/quantum/quantum-hackthon/problem5_results.png',
                dpi=150, bbox_inches='tight')
    print("\nVisualization saved as 'problem5_results.png'")


def main():
    """Main function."""
    print("=" * 60)
    print("PROBLEM 5: QUANTUM ML FOR CLOUD ANOMALY DETECTION")
    print("=" * 60)
    
    # Generate data
    metrics, labels = generate_cloud_metrics(100)
    
    print(f"\nGenerated {len(metrics)} samples")
    print(f"Normal: {(labels == 0).sum()}")
    print(f"Anomalies: {(labels == 1).sum()}")
    
    # Run quantum anomaly detection
    print("\nRunning quantum anomaly detection...")
    predictions = []
    
    for i in range(len(metrics)):
        # Use all other points as reference
        ref_metrics = np.delete(metrics, i, axis=0)
        ref_labels = np.delete(labels, i)
        
        pred, _ = quantum_anomaly_detector(ref_metrics, ref_labels, metrics[i])
        predictions.append(pred)
    
    predictions = np.array(predictions)
    
    # Visualize
    visualize_results(metrics, labels, predictions)
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"\nSamples: {len(metrics)}")
    print(f"Anomalies detected: {(predictions > 0.5).sum()}")
    print(f"Actual anomalies: {(labels == 1).sum()}")
    print("\n✓ Problem 5 completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
