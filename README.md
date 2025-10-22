# Quantum Walk-Based Influence Maximization in Social Networks

## Overview

Quantum walk-based algorithm for influence maximization in social networks using Qiskit.Identifies influential nodes via quantum interference in scale-free networks.Built with Python, NetworkX, NumPy, SciPy, Matplotlib.Features visualizations and modular code for quantum computing research.

## Features


Quantum Walk Algorithm: Implements continuous-time quantum walk to identify influential nodes via quantum interference.
Qiskit Integration: Uses Qiskit for quantum circuit design and simulation, showcasing quantum programming proficiency.
Influence Simulation: Includes linear threshold model to simulate influence spread from selected nodes.
Visualization: Provides network visualizations and probability distributions using NetworkX and Matplotlib.
Modular Design: Structured code with clear functions for reusability and collaboration.
Novelty: Applies quantum walks to influence maximization, an underexplored area in quantum computing.


## Repository Structure


quantum_walk_influence_maximization.py: Main script for the quantum walk-based influence maximization algorithm.
requirements.txt: Lists dependencies (qiskit, networkx, numpy, matplotlib, scipy).
.gitignore: Ignores Python-related artifacts (e.g., pycache, virtual environments).
README.md: Project documentation.


## Installation


Clone the repository:git clone https://github.com/pradeepdegalaroyal/quantum-walk-influence-maximization.git
cd quantum-walk-influence-maximization


Create a virtual environment (optional but recommended):python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:pip install -r requirements.txt


Run the script:python quantum_walk_influence_maximization.py




## Usage


Creates a scale-free social network with 10 nodes using the Barabási-Albert model.
Modify create_social_network(n_nodes) to adjust network size or structure (e.g., real-world data).
Adjust parameters in the main block:
n_nodes: Number of nodes/qubits (default: 10).
t: Quantum walk evolution time (default: 1.0).
shots: Number of simulation shots (default: 1024).
top_k: Number of influential nodes to select (default: 3).


Outputs influential nodes, their influence scores, simulated influence spread, and visualizations.


## Results


Identifies top k influential nodes based on quantum walk measurement probabilities.
Visualizes:
Network with influential nodes highlighted in red.
Bar plot of probabilities per node, with influential nodes in red.


Simulates influence spread using a linear threshold model, reporting activated nodes.


## Example Output

Influential nodes: [2, 4, 7]Influence scores: [0.142578125, 0.150390625, 0.16796875]Influence spread: 8 nodes activated

## Future Improvements


Optimize quantum walk evolution time t using classical optimization (e.g., SPSA).
Incorporate real-world social network datasets for practical applications.
Add error mitigation for noisy quantum simulations.
Explore hybrid quantum-classical approaches with variational algorithms.
Extend to larger networks or multi-step quantum walks.


## Dependencies


Python 3.8+
Qiskit 0.44.0
NetworkX 3.0
NumPy 1.24.0
Matplotlib 3.7.0
SciPy 1.10.0


## Contributing

Contributions are welcome! Please:

Fork the repository.
Create a feature branch (git checkout -b feature/YourFeature).
Commit changes (git commit -m 'Add YourFeature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request.


## License

MIT License

## Author

[Your Name] - Quantum Computing Enthusiast and Qiskit AdvocateEmail: your.email@example.comGitHub: github.com/your-username

