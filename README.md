# Network Assisted Quantum Key Distribution (QKD)

## Overview

This project implements a **Network-Assisted Quantum Key Distribution (QKD)** framework that studies secret key generation under realistic noisy quantum communication environments.

The framework integrates:
- Physical channel characteristics
- Network-level parameters
- Optimization techniques
- Simulation-based analysis

to estimate and improve achievable secret key rates in QKD networks.

---

## Features

- Simulation of QKD communication channels
- Estimation of secret key rates
- Network-assisted parameter optimization
- Noise-aware performance analysis
- Visualization of simulation results
- Modular Python implementation

---

## Project Structure

```
NetworkAssistedQKD/
│
├── main.py              # Main execution file
├── simulation.py        # QKD simulation framework
├── optimizer.py         # Optimization algorithms
├── parameters.py        # System and simulation parameters
├── plots.py             # Result visualization
├── utils.py             # Utility functions
├── requirements.txt     # Required Python packages
└── README.md            # Project documentation
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/amulyav0546-cpu/qkd.git
```

Navigate to the project directory:

```bash
cd qkd
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the environment:

### Linux/macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the main simulation:

```bash
python main.py
```

The simulation outputs performance metrics and generated plots for analyzing QKD network performance.

---

## Methodology

The framework follows these major steps:

1. Define quantum channel and network parameters.
2. Simulate QKD communication under noisy conditions.
3. Estimate achievable secret key rates.
4. Optimize network-assisted parameters.
5. Analyze performance through generated results.

---

## Technologies Used

- Python
- NumPy
- SciPy
- Matplotlib
- Quantum Communication Concepts
- Optimization Algorithms

---

## Applications

This project can support research in:

- Secure quantum communication networks
- Future quantum internet architectures
- Network-assisted QKD optimization
- Quantum cryptography performance analysis

---

## Future Improvements

- Integration with real QKD hardware parameters
- Advanced optimization algorithms
- Machine learning based key-rate prediction
- Large-scale quantum network simulations

---

## License

This project is intended for academic and research purposes.
